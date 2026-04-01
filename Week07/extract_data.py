import os
import sys
import pandas as pd
from sqlalchemy import text

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_ROOT)

from app.db import get_engine
from app.config import settings


def extract_leads() -> pd.DataFrame:
    query = text("""
        SELECT
            l.id,
            l.name,
            l.source,
            l.course_service,
            l.gender,
            l.location,
            l.phone,
            l.stage,
            l.contacted_at,
            l.created_at,
            l.referral_id,
            l.notes,
            r.user_id AS referral_user_id,
            r.name AS referral_name,
            r.phone AS referral_phone,
            r.email AS referral_email,
            c.id AS client_id,
            c.name AS client_name,
            c.location AS client_location,
            c.lead_id AS client_lead_id
        FROM leads l
        LEFT JOIN referrals r ON l.referral_id = r.id
        LEFT JOIN clients c ON l.id = c.lead_id
    """)
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


def extract_payments() -> pd.DataFrame:
    query = text("""
        SELECT
            p.id,
            p.amount,
            p.date,
            p.payment_type,
            p.category,
            p.client_id,
            p.purpose
        FROM payments p
    """)
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


def extract_installments() -> pd.DataFrame:
    query = text("""
        SELECT
            spi.id,
            spi.amount,
            spi.date_paid,
            spi.due_date,
            spi.installment_number,
            spi.sales_payment_record_id
        FROM sales_payment_installments spi
    """)
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


def save_all_raw_data():
    os.makedirs(settings.DATA_DIR, exist_ok=True)

    leads = extract_leads()
    leads.to_csv(os.path.join(settings.DATA_DIR, "raw_leads.csv"), index=False)
    print(f"Saved raw leads: {leads.shape}")

    payments = extract_payments()
    payments.to_csv(os.path.join(settings.DATA_DIR, "raw_payments.csv"), index=False)
    print(f"Saved raw payments: {payments.shape}")

    installments = extract_installments()
    installments.to_csv(os.path.join(settings.DATA_DIR, "raw_installments.csv"), index=False)
    print(f"Saved raw installments: {installments.shape}")


if __name__ == "__main__":
    save_all_raw_data()
