from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
CORS(app)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json

    def extract_features(d):
        return [
            d.get("mouse_speed", 0),
            d.get("mouse_angle", 0),
            d.get("mouse_angle_var", 0),
            d.get("mouse_accel", 0),
            d.get("click_interval", 0),
            d.get("key_dwell_time", 0),
            d.get("key_flight_time", 0),
            d.get("nav_method", 0)
        ]

    history = [extract_features(d) for d in data["history"]]
    current = [extract_features(data["current"])]

    # 🔐 Phishing detection based on submit method
    training_methods = [d.get("submit_method", "mouse") for d in data["history"]]
    most_common_method = max(set(training_methods), key=training_methods.count)
    current_method = data["current"].get("submit_method", "mouse")

    print("Training method:", most_common_method)
    print("Current method:", current_method)

    if current_method != most_common_method:
        return jsonify({
            "risk_score": 1.0,
            "match": "🚨 Phishing Detected: Submit method changed"
        })

    # Simulated impostors
    impostors = np.array([
        [2.5, 180, 3000, 5.0, 0.1, 0.02, 0.01, 1],
        [0.1, 0, 0.5, -1.0, 1.0, 0.5, 0.4, 0],
        [3.0, 90, 2000, 4.5, 0.2, 0.03, 0.02, 1]
    ])

    X = np.vstack([history, impostors])
    y = np.array([0] * len(history) + [1] * len(impostors))

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)

    risk_score = clf.predict_proba(current)[0][1]
    match = "✅ Same person" if risk_score < 0.5 else "🚨 Behavior mismatch"

    return jsonify({
        "risk_score": round(risk_score, 2),
        "match": match
    })

if __name__ == "__main__":
    print("🚀 Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True)
