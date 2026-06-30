import pandas as pd
import pickle

# ✅ CORRECT DATASET LOADING (IMPORTANT FIX)
df = pd.read_csv(
    "SMSSpamCollection.txt",   # <-- make sure file is .txt
    sep='\t',
    header=None,
    names=["label", "message"],
    encoding='latin-1'
)

# ✅ DEBUG (CHECK DATA LOADING)
print("Total rows:", len(df))
print(df.head())

# ✅ Fill missing messages (DO NOT drop all rows)
df['message'] = df['message'].fillna("")

# ✅ Convert labels
df['label'] = df['label'].map({'ham': 'Safe', 'spam': 'Scam'})

# ✅ Add Suspicious class
def mark_suspicious(text):
    keywords = ["verify", "update", "urgent", "account", "bank", "password"]
    for word in keywords:
        if word in text.lower():
            return "Suspicious"
    return None

df['label'] = df.apply(
    lambda row: "Suspicious" if mark_suspicious(row['message']) else row['label'],
    axis=1
)

# ✅ Convert labels to numeric
df['label'] = df['label'].map({
    'Safe': 0,
    'Suspicious': 1,
    'Scam': 2
})

# ✅ Remove invalid rows only
df = df.dropna(subset=['label'])

# ✅ CHECK CLASS DISTRIBUTION
print("Class Distribution:\n", df['label'].value_counts())

# ❌ STOP if dataset is wrong
if len(df) < 100:
    print("❌ ERROR: Dataset not loaded properly")
    exit()

# ✅ Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# ✅ Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_features=5000
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ✅ Model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=500, class_weight='balanced')

model.fit(X_train_vec, y_train)

# ✅ Accuracy
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ✅ Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully!")