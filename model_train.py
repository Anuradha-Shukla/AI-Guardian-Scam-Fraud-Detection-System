import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# -----------------------------
# SAMPLE DATASET (you can later replace with Kaggle dataset)
# -----------------------------
data = {
    "text": [
        "Your account is blocked click here",
        "You won lottery claim now",
        "OTP shared fraud detected",
        "UPI payment done successfully",
        "Salary credited to account",
        "New device login detected",
        "Multiple OTP requests received",
        "Amazon order delivered",
        "Bank fraud detected",
        "Payment successful for groceries"
    ],
    "label": [
        "FRAUD",
        "FRAUD",
        "FRAUD",
        "SAFE",
        "SAFE",
        "SUSPICIOUS",
        "SUSPICIOUS",
        "SAFE",
        "FRAUD",
        "SAFE"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# TEXT VECTORIZATION (NLP)
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# -----------------------------
# MODEL TRAINING
# -----------------------------
model = LogisticRegression()
model.fit(X, df["label"])

# -----------------------------
# SAVE MODEL
# -----------------------------
joblib.dump(model, "fraud_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")