from app.lead_scoring.train import train_best_model


if __name__ == "__main__":
    result = train_best_model()
    print(f"Retrained lead model: {result['model_name']}")
