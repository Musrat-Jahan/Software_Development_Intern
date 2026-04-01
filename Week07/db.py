from sqlalchemy import create_engine
from app.config import settings


def get_connection_url() -> str:
    return (
        f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
        f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    )


def get_engine():
    return create_engine(get_connection_url())
