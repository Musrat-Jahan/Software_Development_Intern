from __future__ import annotations
import json
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from app.config import settings
from app.revenue_forecasting.data import fetch_revenue_tables

MODEL_PATH = settings.model_dir / "revenue_model.joblib"


def build_monthly_revenue(payments: pd.DataFrame) -> pd.DataFrame:
    payments = payments.copy()
    payments["date"] = pd.to_datetime(payments["date"], errors="coerce")
    payments = payments.dropna(subset=["date"])
    payments["month"] = payments["date"].dt.to_period("M").dt.to_timestamp()
    monthly = payments.groupby("month", as_index=False)["amount"].sum().sort_values("month")
    monthly["month_index"] = range(len(monthly))
    return monthly


def train_revenue_model() -> dict:
    payments, installments, records = fetch_revenue_tables()
    monthly = build_monthly_revenue(payments)

    if len(monthly) < 2:
        monthly = pd.DataFrame({"month": [pd.Timestamp.today().to_period('M').to_timestamp()], "amount": [0.0], "month_index": [0]})

    X = monthly[["month_index"]]
    y = monthly["amount"]
    model = LinearRegression()
    model.fit(X, y)

    installment_future = 0.0
    if not installments.empty:
        installments["due_date"] = pd.to_datetime(installments["due_date"], errors="coerce")
        future_installments = installments[installments["due_date"] >= pd.Timestamp.today().normalize()]
        installment_future = float(future_installments["amount"].fillna(0).sum())

    payload = {
        "model": model,
        "history": monthly.to_dict(orient="records"),
        "training_rows": int(len(monthly)),
        "installment_future_total": installment_future,
        "model_name": "linear_regression_monthly_revenue",
    }
    joblib.dump(payload, MODEL_PATH)
    return payload


if __name__ == "__main__":
    result = train_revenue_model()
    print(json.dumps({
        "saved_to": str(MODEL_PATH),
        "model_name": result["model_name"],
        "training_rows": result["training_rows"],
    }, indent=2))
