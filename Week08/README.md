# MetroBlue ML Service

Standalone FastAPI service for MetroBlue that:
- trains a lead scoring model from `leads`, `referrals`, and `clients`
- builds a simple revenue forecasting model from `payments` and installment data
- exposes REST API endpoints the main MetroBlue app can call
- shows a lightweight dashboard in the browser

## Project structure

```text
metroblue_ml_service/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── config.py
│   ├── schemas.py
│   ├── templates/
│   │   └── dashboard.html
│   ├── models/
│   │   ├── lead_model.joblib
│   │   └── revenue_model.joblib
│   ├── lead_scoring/
│   │   ├── data.py
│   │   ├── features.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── retrain.py
│   └── revenue_forecasting/
│       ├── data.py
│       ├── train.py
│       └── predict.py
├── tests/
│   ├── test_health.py
│   └── test_lead_predictor.py
├── scripts/
│   └── bootstrap_models.py
├── requirements.txt
└── .env.example
```

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# or
venv\Scriptsctivate      # Windows PowerShell

pip install -r requirements.txt
cp .env.example .env
```

Update `.env` with your real MySQL connection string.

## Train models

```bash
python -m app.lead_scoring.train
python -m app.revenue_forecasting.train
```

Or bootstrap both:

```bash
python scripts/bootstrap_models.py
```

## Run API

```bash
uvicorn app.main:app --reload
```

Open:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## API endpoints

- `GET /health`
- `GET /`
- `POST /predict-lead`
- `GET /lead-model-info`
- `GET /revenue-forecast?months=3`
- `GET /revenue-model-info`

## Lead model features

- source one-hot
- course/service one-hot
- gender binary
- has_location
- top-N location one-hot
- has_phone
- has_referral
- referral_lead_count
- days_since_contacted
- days_since_created
- contact_speed
- notes_length
- has_notes
- created_day_of_week
- created_month

## Notes

- If your database is empty, the training scripts create a small fallback sample dataset so the service can still run locally.
- Revenue forecasting is intentionally simple and transparent: it predicts monthly revenue using historical monthly totals and expected installment revenue.
- For production, store trained `.joblib` files in a persistent location and retrain on a schedule.
