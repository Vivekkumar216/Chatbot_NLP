import os
import json
import random
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Global variables for the model
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X_train = None
tags = []
intents = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load intents and train model on startup
    global intents, X_train, tags
    file_path = os.path.abspath("./intents.json")
    with open(file_path, "r", encoding="utf-8") as file:
        intents = json.load(file)
    
    tags = []
    patterns = []
    for intent in intents:
        for pattern in intent["patterns"]:
            tags.append(intent["tag"])
            patterns.append(pattern)
            
    X_train = vectorizer.fit_transform(patterns)
    print("Chatbot model trained successfully.")
    
    yield

app = FastAPI(lifespan=lifespan)

# Allow CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    input_text = req.message
    if not input_text.strip():
        return ChatResponse(response="Please say something.")
        
    input_vec = vectorizer.transform([input_text])
    similarities = cosine_similarity(input_vec, X_train)[0]
    
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]
    
    # If the match score is above 30%, we return the matched intent's response
    if best_score > 0.3:
        tag = tags[best_idx]
        for intent in intents:
            if intent['tag'] == tag:
                response = random.choice(intent['responses'])
                return ChatResponse(response=response)
                
    return ChatResponse(response="I'm sorry, I don't understand that.")

# Mount the frontend built files (if they exist)
frontend_dist = os.path.join(os.path.dirname(__file__), "frontend", "dist")
if os.path.exists(frontend_dist):
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")
else:
    @app.get("/")
    async def root():
        return {"message": "Frontend not built yet. Run 'npm run build' in the frontend directory."}

if __name__ == "__main__":
    import uvicorn
    # Use the PORT environment variable if it exists (for deployment), otherwise default to 8000
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)
