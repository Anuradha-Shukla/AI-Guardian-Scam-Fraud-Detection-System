# AI Guardian - Scam & Fraud Detection System 🚨

An AI-powered web application that detects scam, fraud, and suspicious messages using Machine Learning and Natural Language Processing.

The system analyzes user messages, identifies potential threats, provides confidence scores, stores scan history, and displays analytics for detected patterns.

## 🚀 Live Demo

🔗 https://ai-guardian-scam-fraud-detection-system.onrender.com


## ✨ Features

- 🚨 Scam/Fraud message detection
- ⚠️ Suspicious activity identification
- 🤖 Machine Learning based classification
- 📊 Confidence score prediction
- 📝 Scan history management
- 📈 Analytics dashboard
- 🔍 Explainable AI using suspicious keyword detection
- 💾 SQLite database integration


## 🧠 How It Works

1. User enters a message for analysis.
2. Text is converted into numerical features using TF-IDF Vectorization.
3. ML model analyzes the message patterns.
4. The system classifies it as:
   - SAFE
   - FRAUD
   - SUSPICIOUS
5. Result and scan history are stored in the database.


## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Gunicorn

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Naive Bayes Classification
- Joblib

### Database
- SQLite

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js


## 📂 Project Structure
