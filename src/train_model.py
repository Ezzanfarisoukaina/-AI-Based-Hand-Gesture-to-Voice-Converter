
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Charger le dataset
DATASET_PATH = "data/gestures/gestures.csv"

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

# 2. Separar les features et les labels
X = df.drop("label", axis=1)
y = df["label"]

# 3. Diviser les donnees
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Creer le modele
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 5. Entrainer le modele
print("\nTraining model...")
model.fit(X_train, y_train)

# 6. Faire les predictions
y_pred = model.predict(X_test)

# 7. Evaluer le modele
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 8. Sauvegarder le modele
import os

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/gesture_model.pkl")

print("\nModel saved successfully!")
