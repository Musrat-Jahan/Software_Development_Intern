from __future__ import annotations
import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db import get_engine

PAYMENTS_QUERY = """
SELECT amount, date, payment_type, category, client_id, purpose
FROM payments
"""
INSTALLMENTS_QUERY = """
SELECT amount, date_paid, due_date, installment_number
FROM sales_payment_installments
"""
RECORDS_QUERY = """
SELECT total_amount, balance, due_date, client_id
FROM sales_payment_records
"""


def sample_revenue_data():
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=12, freq="MS")
    payments = pd.DataFrame({
        "date": dates,
        "amount": [12000, 15000, 14500, 16000, 17250, 18000, 19400, 21000, 20500, 22300, 24000, 25000],
        "payment_type": "Paid",
        "category": "Service",
        "client_id": range(1, 13),
        "purpose": "Sample"
    })
    installments = pd.DataFrame({
        "amount": [3000, 3200, 2800],
        "date_paid": [None, None, None],
        "due_date": [pd.Timestamp.today() + pd.offsets.MonthBegin(1), pd.Timestamp.today() + pd.offsets.MonthBegin(2), pd.Timestamp.today() + pd.offsets.MonthBegin(3)],
        "installment_number": [1, 2, 3],
    })
    records = pd.DataFrame({
        "total_amount": [9000],
        "balance": [4500],
        "due_date": [pd.Timestamp.today() + pd.offsets.MonthBegin(1)],
        "client_id": [99],
    })
    return payments, installments, records


def fetch_revenue_tables():
    try:
        engine = get_engine()
        with engine.connect() as conn:
            payments = pd.read_sql(text(PAYMENTS_QUERY), conn)
            installments = pd.read_sql(text(INSTALLMENTS_QUERY), conn)
            records = pd.read_sql(text(RECORDS_QUERY), conn)
        if payments.empty:
            return sample_revenue_data()
        return payments, installments, records
    except SQLAlchemyError:
        return sample_revenue_data()
