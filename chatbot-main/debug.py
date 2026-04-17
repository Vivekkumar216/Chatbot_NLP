import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

file_path = os.path.abspath("./intents.json")
with open(file_path, "r", encoding="utf-8") as file:
    intents = json.load(file)

tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)
        
vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(patterns)
y = tags

clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(x, y)

y_pred = clf.predict(x)
print(f"Training Accuracy: {accuracy_score(y, y_pred) * 100:.2f}%")

# Let's test a few common ones
test_cases = [
    "Hello",
    "How are you",
    "What can you do",
    "Thank you"
]

print("\n--- Predictions ---")
for text in test_cases:
    vec = vectorizer.transform([text])
    tag = clf.predict(vec)[0]
    probs = clf.predict_proba(vec)[0]
    max_prob = max(probs)
    print(f"'{text}' -> Tag: {tag} (Confidence: {max_prob*100:.2f}%)")
