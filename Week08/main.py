from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.schemas import LeadPayload, LeadPredictionResponse, RevenueForecastResponse
from app.lead_scoring.predict import score_lead, load_artifacts as load_lead_artifacts
from app.revenue_forecasting.predict import forecast_revenue, load_artifacts as load_revenue_artifacts

app = FastAPI(title="MetroBlue ML Service", version="1.0.0")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/health")
def health():
    return {"status": "ok", "service": "metroblue-ml-service"}


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    lead_status = "available"
    revenue_status = "available"
    try:
        load_lead_artifacts()
    except Exception:
        lead_status = "not available"
    try:
        load_revenue_artifacts()
    except Exception:
        revenue_status = "not available"
    return templates.TemplateResponse("dashboard.html", {"request": request, "lead_status": lead_status, "revenue_status": revenue_status})


@app.post("/predict-lead", response_model=LeadPredictionResponse)
def predict_lead(payload: LeadPayload):
    return score_lead(payload.model_dump())


@app.get("/lead-model-info")
def lead_model_info():
    artifacts = load_lead_artifacts()
    return {
        "model_name": artifacts.get("model_name"),
        "training_rows": artifacts.get("training_rows"),
        "metrics": artifacts.get("metrics"),
        "feature_columns": artifacts.get("feature_columns"),
        "top_feature_importance": artifacts.get("feature_importances"),
    }


@app.get("/revenue-forecast", response_model=RevenueForecastResponse)
def revenue_forecast(months: int = 3):
    return {"months_requested": months, "forecast": forecast_revenue(months=months)}


@app.get("/revenue-model-info")
def revenue_model_info():
    artifacts = load_revenue_artifacts()
    return {
        "model_name": artifacts.get("model_name"),
        "training_rows": artifacts.get("training_rows"),
        "installment_future_total": artifacts.get("installment_future_total"),
    }
