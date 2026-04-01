import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from app.revenue_model import train_revenue_model


def main():
    df = pd.read_csv("data/raw_payments.csv")

    metadata = train_revenue_model(df)

    print("Revenue model trained successfully")
    print(metadata)


if __name__ == "__main__":
    main()