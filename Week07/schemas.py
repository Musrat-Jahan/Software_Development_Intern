from __future__ import annotations

from typing import Optional
from pydantic import BaseModel


class LeadPredictionRequest(BaseModel):
    id: Optional[int] = 0
    source: Optional[str] = None
    course_service: Optional[str] = None
    gender: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None
    stage: Optional[str] = "unknown"
    contacted_at: Optional[str] = None
    created_at: Optional[str] = None
    referral_id: Optional[int] = None
    notes: Optional[str] = None


class LeadPredictionResponse(BaseModel):
    prediction: int
    probability_converted: float
    probability_not_converted: float
