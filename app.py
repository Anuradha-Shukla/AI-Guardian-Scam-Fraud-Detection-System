from flask import Flask, render_template, request
import joblib
import sqlite3

app = Flask(__name__)

# ================= LOAD MODEL =================
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# ================= DB SETUP =================
def init_db():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT,
            result TEXT
        )
    """)

    conn.commit()
    conn.close()

init_db()


# ================= HOME =================
@app.route('/')
def home():
    return render_template('home.html')


# ================= SCAN =================
@app.route('/scan', methods=['GET', 'POST'])
def scan():
    result = None
    reasons = []

    if request.method == 'POST':
        message = request.form['message']

        input_vector = vectorizer.transform([message])
        prediction = model.predict(input_vector)[0]

        probabilities = model.predict_proba(input_vector)[0]
        confidence = max(probabilities) * 100

        label_map = {
            0: "SAFE",
            1: "FRAUD",
            2: "SUSPICIOUS"
        }

        label = label_map.get(prediction, "UNKNOWN")

        # Explainability
        fraud_words = ["otp", "click here", "verify", "blocked", "urgent", "bank"]
        suspicious_words = ["login", "device", "unknown", "location", "attempt"]

        msg = message.lower()

        for w in fraud_words:
            if w in msg:
                reasons.append(f'Suspicious keyword: "{w}"')

        for w in suspicious_words:
            if w in msg:
                reasons.append(f'Behavior anomaly: "{w}"')

        if not reasons:
            reasons.append("No suspicious indicators detected")

        result = f"{label} ({confidence:.2f}% confidence)"

        # ================= SAVE TO DATABASE =================
        conn = sqlite3.connect("history.db")
        c = conn.cursor()

        c.execute("INSERT INTO scans (message, result) VALUES (?, ?)", (message, result))

        conn.commit()
        conn.close()

    return render_template('scan.html', result=result, reasons=reasons)


# ================= HISTORY =================
@app.route('/history')
def history():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()

    c.execute("SELECT message, result FROM scans ORDER BY id DESC")
    data = c.fetchall()

    conn.close()

    return render_template('history.html', data=data)


# ================= ANALYTICS =================
@app.route('/analytics')
def analytics():
    conn = sqlite3.connect("history.db")
    c = conn.cursor()

    c.execute("SELECT result FROM scans")
    rows = c.fetchall()

    conn.close()

    total = len(rows)

    fraud_count = len([r for r in rows if "FRAUD" in r[0]])
    suspicious_count = len([r for r in rows if "SUSPICIOUS" in r[0]])
    safe_count = len([r for r in rows if "SAFE" in r[0]])

    fraud_percent = (fraud_count / total * 100) if total else 0
    suspicious_percent = (suspicious_count / total * 100) if total else 0
    safe_percent = (safe_count / total * 100) if total else 0

    return render_template(
        'analytics.html',
        total=total,
        fraud_count=fraud_count,
        suspicious_count=suspicious_count,
        safe_count=safe_count,
        fraud_percent=fraud_percent,
        suspicious_percent=suspicious_percent,
        safe_percent=safe_percent
    )


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)




