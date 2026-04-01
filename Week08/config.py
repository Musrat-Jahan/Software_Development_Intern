from pathlib import Path
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./metroblue.db")
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8000"))
    model_dir: Path = Path(os.getenv("MODEL_DIR", "app/models"))
    top_n_locations: int = int(os.getenv("TOP_N_LOCATIONS", "10"))


settings = Settings()
settings.model_dir.mkdir(parents=True, exist_ok=True)
