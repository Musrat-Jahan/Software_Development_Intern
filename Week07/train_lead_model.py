import os
import sys
import pandas as pd

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.append(PROJECT_ROOT)

from app.config import settings
from app.lead_model import train_lead_model


def main():
    path = os.path.join(settings.DATA_DIR, "processed_leads.csv")
    df = pd.read_csv(path)
    metrics = train_lead_model(df)
    print("Lead model trained.")
    print(metrics)


if __name__ == "__main__":
    main()
