from app.lead_scoring.train import train_best_model
from app.revenue_forecasting.train import train_revenue_model


if __name__ == "__main__":
    lead = train_best_model()
    revenue = train_revenue_model()
    print("Lead model:", lead["model_name"])
    print("Revenue model:", revenue["model_name"])
