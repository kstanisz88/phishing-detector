import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("dataset_phishing.csv")
df = df.drop(columns=["url"])
df["status"] = LabelEncoder().fit_transform(df["status"])

# Split features and target
X = df.drop(columns=["status"])
y = df["status"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "phishing_model.pkl")
