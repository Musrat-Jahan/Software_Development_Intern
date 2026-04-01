import os
import joblib
import pandas as pd

MODEL_PATH = "models/revenue_forecast_model.pkl"


def train_revenue_model(df):
    if "date" not in df.columns or "amount" not in df.columns:
        raise ValueError("Revenue data must contain 'date' and 'amount' columns.")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount"])

    monthly_revenue = (
        df.groupby(df["date"].dt.to_period("M"))["amount"]
        .sum()
        .reset_index()
    )

    monthly_revenue["date"] = monthly_revenue["date"].astype(str)

    if len(monthly_revenue) < 3:
        baseline_value = float(monthly_revenue["amount"].mean()) if len(monthly_revenue) > 0 else 0.0
        os.makedirs("models", exist_ok=True)
        joblib.dump(
            {"baseline_monthly_revenue": baseline_value},
            MODEL_PATH
        )
        return {
            "baseline_monthly_revenue": baseline_value,
            "note": "Fallback model used due to limited data"
        }

    baseline_value = float(monthly_revenue["amount"].mean())

    os.makedirs("models", exist_ok=True)
    joblib.dump(
        {"baseline_monthly_revenue": baseline_value},
        MODEL_PATH
    )

    return {
        "baseline_monthly_revenue": baseline_value,
        "months_used": int(len(monthly_revenue))
    }


def load_revenue_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Revenue model file not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def forecast_next_months(model, months=3):
    baseline_value = float(model.get("baseline_monthly_revenue", 0.0))
    return {
        "forecast_months": months,
        "predictions": [baseline_value for _ in range(months)]
    }