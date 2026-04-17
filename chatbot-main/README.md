# Chatbot NLP 🤖 | Your Personalized Guide

**Chatbot NLP** is an intuitive chatbot designed to bridge the gap between curiosity and knowledge. Whether you're exploring program details or seeking guidance, this chatbot is here to assist you with a lightning-fast, modern web interface.

---

## ✨ Key Features
- 🔍 **Intent Classification**: Understands and classifies user queries into specific intents using `scikit-learn`'s Logistic Regression.
- ⚡ **Zero-Latency Backend**: Powered by **FastAPI** to ensure responses are delivered almost instantaneously.
- 🎨 **Premium User Interface**: A beautifully designed, glassmorphic dark-mode web application built with **React** and **Vite**.
- 💬 **Interactive Chat**: Engage in real-time conversations via a sleek, modern UI.

---

## 🔧 Technology Stack

### Backend
- **Programming Language**: Python
- **Framework**: FastAPI
- **Libraries and Tools**:
  - `nltk` for text preprocessing (tokenization, stemming, stop-word removal).
  - `scikit-learn` for intent classification using Logistic Regression and TF-IDF.

### Frontend
- **Framework**: React (via Vite)
- **Styling**: Vanilla CSS with glassmorphism and modern micro-animations.

---

## 🚀 Run the Project Locally

The entire application (both the machine learning backend and the React frontend) is served from a single Python server!

1. Open a terminal in the project directory.
2. Install the backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```bash
   python server.py
   ```
4. Open your browser and navigate to:
   **http://localhost:8000**

*(Note: If you wish to make changes to the frontend UI, navigate to the `frontend/` folder, run `npm install`, and then `npm run dev` to start the Vite development server.)*

---

## 🚀 How It Works

### 1. Preprocessing & Training
- The application loads a dataset of intents, patterns, and responses from `intents.json`.
- It processes and vectorizes the text using TF-IDF.
- Logistic Regression is trained on startup to classify user inputs into predefined categories.

### 2. Response Generation
- Based on the classified intent from the FastAPI `/api/chat` endpoint, the chatbot fetches and delivers a relevant response back to the user.

### 3. User Interface
The **React** frontend provides a clean, minimalistic, and highly responsive interface with chat history and typing indicators, making the chatbot accessible and fun to use.

---

## ☁️ Deployment (Cloud)

To deploy this project to the web for free, I recommend using **[Render.com](https://render.com/)**:

1. Create a free account on Render.
2. Create a **New Web Service** and connect your GitHub repo.
3. Select **Python** as the environment.
4. Set the **Build Command** to:
   ```bash
   pip install -r requirements.txt && cd frontend && npm install && npm run build
   ```
5. Set the **Start Command** to:
   ```bash
   python server.py
   ```
6. Your app will be live at a `.onrender.com` URL!

---

## 📬 Contact

Have questions or feedback? Let’s connect!

- **Author**: Vivek Kumar
- **GitHub Repo**: [Chatbot_NLP](https://github.com/Vivekkumar216/Chatbot_NLP)
