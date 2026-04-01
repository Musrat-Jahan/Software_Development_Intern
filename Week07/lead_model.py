import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


MODEL_PATH = "models/lead_conversion_model.pkl"


def train_lead_model(df):
    df = df.copy()

    if "stage" in df.columns:
        df["converted"] = (df["stage"].astype(str).str.strip().str.lower() == "paid").astype(int)
    elif "converted" not in df.columns:
        raise Exception("Target column not found. Expected 'stage' or 'converted'.")

    y = df["converted"]
    X = df.drop(columns=[c for c in ["stage", "converted"] if c in df.columns], errors="ignore")

    if len(df) < 10:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.4, random_state=42
        )
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    return {"accuracy": acc}


def load_lead_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Lead model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)