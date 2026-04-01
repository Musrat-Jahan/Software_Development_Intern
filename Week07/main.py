from __future__ import annotations

import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.config import settings
from app.feature_builder import build_single_prediction_row
from app.lead_model import load_lead_model, MODEL_PATH as LEAD_MODEL_PATH
from app.revenue_model import load_revenue_model, forecast_next_months, MODEL_PATH as REV_MODEL_PATH
from app.schemas import LeadPredictionRequest

app = FastAPI(title="MetroBlue ML Service", version="1.0.0")


def _safe_load_processed_revenue() -> pd.DataFrame:
    path = os.path.join(settings.DATA_DIR, "monthly_revenue.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        if "month" in df.columns:
            df["month"] = pd.to_datetime(df["month"], errors="coerce")
        return df
    return pd.DataFrame()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def dashboard():
    lead_status = "available" if os.path.exists(LEAD_MODEL_PATH) else "not trained"
    revenue_status = "available" if os.path.exists(REV_MODEL_PATH) else "not trained"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset=\"utf-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
        <title>MetroBlue ML Service</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f6f8fb; color: #222; }}
            .card {{ background: white; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.06); }}
            code {{ background: #f0f3f7; padding: 2px 6px; border-radius: 6px; }}
        </style>
    </head>
    <body>
        <div class=\"card\">
            <h1>MetroBlue ML Service</h1>
            <p>Lead model: <strong>{lead_status}</strong></p>
            <p>Revenue model: <strong>{revenue_status}</strong></p>
        </div>
        <div class=\"card\">
            <h2>Available endpoints</h2>
            <p><code>GET /health</code></p>
            <p><code>POST /predict-lead</code></p>
            <p><code>GET /lead-model-info</code></p>
            <p><code>GET /revenue-forecast?months=3</code></p>
            <p><code>GET /revenue-model-info</code></p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.post("/predict-lead")
def predict_lead(payload: LeadPredictionRequest):
    if not os.path.exists(LEAD_MODEL_PATH):
        raise HTTPException(status_code=400, detail="Lead model not trained yet.")

    model, features, _metrics = load_lead_model()
    input_df = build_single_prediction_row(payload.model_dump(), features)
    prediction = int(model.predict(input_df)[0])
    probabilities = model.predict_proba(input_df)[0]

    return {
        "prediction": prediction,
        "probability_converted": round(float(probabilities[1]), 4),
        "probability_not_converted": round(float(probabilities[0]), 4),
    }


@app.get("/lead-model-info")
def lead_model_info():
    if not os.path.exists(LEAD_MODEL_PATH):
        raise HTTPException(status_code=400, detail="Lead model not trained yet.")
    _model, features, metrics = load_lead_model()
    return {
        "feature_count": len(features),
        "features": features,
        "metrics": metrics,
    }


@app.get("/revenue-model-info")
def revenue_model_info():
    if not os.path.exists(REV_MODEL_PATH):
        raise HTTPException(status_code=400, detail="Revenue model not trained yet.")
    _model, metadata = load_revenue_model()
    return metadata


@app.get("/revenue-forecast")
def revenue_forecast(months: int = 3):
    if not os.path.exists(REV_MODEL_PATH):
        raise HTTPException(status_code=400, detail="Revenue model not trained yet.")

    model, metadata = load_revenue_model()
    monthly = _safe_load_processed_revenue()
    forecasts = forecast_next_months(model, metadata, monthly, periods=months)
    return {"forecasts": forecasts}
