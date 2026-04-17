import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

file_path = os.path.abspath("./intents.json")
with open(file_path, "r", encoding="utf-8") as file:
    intents = json.load(file)

tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)
        
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
x = vectorizer.fit_transform(patterns)

# Let's test a few common ones
test_cases = [
    "Hello",
    "How are you",
    "What can you do",
    "Thank you",
    "Help me please",
    "How old are you"
]

print("\n--- Cosine Similarity Predictions ---")
for text in test_cases:
    vec = vectorizer.transform([text])
    similarities = cosine_similarity(vec, x)[0]
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]
    best_tag = tags[best_idx]
    print(f"'{text}' -> Tag: {best_tag} (Score: {best_score*100:.2f}%)")
