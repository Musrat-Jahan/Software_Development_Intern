import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
PLOTS_DIR = os.path.join(DATA_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


def load_leads() -> pd.DataFrame:
    return pd.read_csv(os.path.join(DATA_DIR, "raw_leads.csv"))


def run_eda():
    df = load_leads()
    df["converted"] = (df["stage"].fillna("").astype(str).str.lower() == "paid").astype(int)

    print("\n=== BASIC INFO ===")
    print(df.info())
    print("\n=== STAGE DISTRIBUTION ===")
    print(df["stage"].value_counts(dropna=False))

    stage_counts = df["stage"].fillna("Unknown").value_counts()
    plt.figure(figsize=(8, 5))
    stage_counts.plot(kind="bar")
    plt.title("Lead Stage Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "stage_distribution.png"))
    plt.close()

    for group_col, filename, title in [
        ("source", "conversion_by_source.png", "Conversion Rate by Source"),
        ("location", "conversion_by_location.png", "Conversion Rate by Location"),
        ("course_service", "conversion_by_service.png", "Conversion Rate by Course/Service"),
    ]:
        grouped = df.groupby(group_col, dropna=False)["converted"].mean().sort_values(ascending=False).head(15)
        print(f"\n=== {group_col.upper()} CONVERSION ===")
        print(grouped)
        plt.figure(figsize=(10, 5))
        grouped.plot(kind="bar")
        plt.title(title)
        plt.tight_layout()
        plt.savefig(os.path.join(PLOTS_DIR, filename))
        plt.close()

    print("EDA complete.")


if __name__ == "__main__":
    run_eda()
