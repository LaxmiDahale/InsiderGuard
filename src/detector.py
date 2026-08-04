import pandas as pd

from sklearn.ensemble import IsolationForest

import joblib


# Load activity logs

df = pd.read_csv(
    "data/user_activity.csv"
)


# Select behavior features

features = [
    "login_hour",
    "failed_logins",
    "files_accessed",
    "download_mb",
    "new_ip"
]


X = df[features]


# Create anomaly model

model = IsolationForest(
    contamination=0.02,
    random_state=42
)


# Train model

model.fit(X)


# Predict

df["prediction"] = model.predict(X)


# Convert prediction

df["status"] = df[
    "prediction"
].map({
    1: "Normal",
    -1: "Suspicious"
})


# Save model

joblib.dump(
    model,
    "models/anomaly_model.pkl"
)


# Save results

df.to_csv(
    "data/detection_results.csv",
    index=False
)


print(
    "Anomaly detection completed."
)