import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import pickle

# Simulated (but expanded) dataset — replace with real data
X = np.array([
    [0.5, 0.3, 0.12, 0.08],
    [0.6, 0.25, 0.11, 0.09],
    [0.55, 0.28, 0.13, 0.07],
    [0.52, 0.32, 0.14, 0.08],
    [1.2, 0.6, 0.25, 0.2],
    [1.1, 0.65, 0.22, 0.18],
    [1.3, 0.7, 0.27, 0.21],
    [1.25, 0.68, 0.26, 0.19]
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:, 1]
print(classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_proba))

# Save model
with open("behavior_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Model trained and saved as behavior_model.pkl")
