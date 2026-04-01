from pydantic import BaseModel, Field
from typing import Any
from datetime import datetime


class LeadPayload(BaseModel):
    source: str | None = None
    course_service: str | None = None
    gender: str | None = None
    location: str | None = None
    phone: str | None = None
    referral_id: int | None = None
    contacted_at: datetime | None = None
    created_at: datetime | None = None
    notes: str | None = None


class LeadPredictionResponse(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0)
    label: str
    factors: list[str]
    top_probability_class: str | None = None
    raw: dict[str, Any] | None = None


class RevenueForecastItem(BaseModel):
    month: str
    predicted_revenue: float


class RevenueForecastResponse(BaseModel):
    months_requested: int
    forecast: list[RevenueForecastItem]
