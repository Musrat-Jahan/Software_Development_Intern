# MetroBlue ML Service

A standalone Python FastAPI service for:
- lead scoring prediction
- revenue forecasting baseline
- REST API endpoints
- simple web dashboard

## Features
- Connects to MetroBlue MySQL database
- Extracts and preprocesses lead and payment data
- Trains a lead conversion model
- Trains a basic revenue forecasting model
- Exposes prediction endpoints with FastAPI
- Includes a lightweight HTML dashboard

## Project Structure

```text
metroblue_ml_service/
├── app/
│   ├── config.py
│   ├── db.py
│   ├── feature_builder.py
│   ├── lead_model.py
│   ├── revenue_model.py
│   ├── schemas.py
│   └── main.py
├── scripts/
│   ├── extract_data.py
│   ├── eda.py
│   ├── preprocess.py
│   ├── train_lead_model.py
│   ├── train_revenue_model.py
│   └── run_all.py
├── data/
├── models/
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Environment
Copy `.env.example` to `.env` and set your DB credentials.

## Run training pipeline

```bash
python scripts/run_all.py
```

## Start API server

```bash
uvicorn app.main:app --reload
```

## Endpoints
- `GET /` dashboard
- `GET /health`
- `POST /predict-lead`
- `GET /lead-model-info`
- `GET /revenue-forecast`
- `GET /revenue-model-info`

## Notes
- This code assumes the database contains the columns described in your project brief.
- If table or column names differ, update the SQL queries accordingly.
- Revenue forecasting here uses a simple regression baseline on monthly revenue. You can improve it later with better time-series methods.
