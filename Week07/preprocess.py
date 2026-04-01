import os
import sys
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_ROOT)

from app.config import settings
from app.feature_builder import build_feature_dataset, select_model_features
from app.revenue_model import prepare_monthly_revenue


def preprocess_leads():
    raw_path = os.path.join(settings.DATA_DIR, "raw_leads.csv")
    df = pd.read_csv(raw_path)
    featured = build_feature_dataset(df)
    model_df = select_model_features(featured)
    model_df.to_csv(os.path.join(settings.DATA_DIR, "processed_leads.csv"), index=False)
    print(f"Processed leads saved: {model_df.shape}")


def preprocess_revenue():
    payments_path = os.path.join(settings.DATA_DIR, "raw_payments.csv")
    installments_path = os.path.join(settings.DATA_DIR, "raw_installments.csv")

    payments = pd.read_csv(payments_path) if os.path.exists(payments_path) else pd.DataFrame()
    installments = pd.read_csv(installments_path) if os.path.exists(installments_path) else pd.DataFrame()
    monthly = prepare_monthly_revenue(payments, installments)
    monthly.to_csv(os.path.join(settings.DATA_DIR, "monthly_revenue.csv"), index=False)
    print(f"Monthly revenue saved: {monthly.shape}")


if __name__ == "__main__":
    preprocess_leads()
    preprocess_revenue()
