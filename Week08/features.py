from __future__ import annotations
import pandas as pd
import numpy as np
from dataclasses import dataclass
from app.config import settings


@dataclass
class LeadFeatureArtifacts:
    feature_columns: list[str]
    top_locations: list[str]
    feature_importances: dict[str, float] | None = None
    metrics: dict | None = None
    model_name: str | None = None


def _clean_dates(df: pd.DataFrame) -> pd.DataFrame:
    for col in ["created_at", "contacted_at"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def add_engineered_features(df: pd.DataFrame, top_locations: list[str] | None = None) -> pd.DataFrame:
    df = df.copy()
    df = _clean_dates(df)
    now = pd.Timestamp.now()

    df["source"] = df.get("source", pd.Series(dtype=object)).fillna("Unknown")
    df["course_service"] = df.get("course_service", pd.Series(dtype=object)).fillna("Unknown")
    df["gender"] = df.get("gender", pd.Series(dtype=object)).fillna("Unknown")
    df["location"] = df.get("location", pd.Series(dtype=object)).fillna("Unknown")
    df["notes"] = df.get("notes", pd.Series(dtype=object)).fillna("")

    df["gender_binary"] = df["gender"].map({"Male": 1, "Female": 0}).fillna(-1).astype(int)
    df["has_location"] = (df["location"].astype(str).str.strip() != "") & (df["location"] != "Unknown")
    df["has_phone"] = df.get("phone", pd.Series(dtype=object)).notna()
    df["has_referral"] = df.get("referral_id", pd.Series(dtype=float)).notna()
    df["referral_lead_count"] = df.groupby("referral_id")["id"].transform("count").fillna(0)
    df["days_since_contacted"] = (now - df["contacted_at"]).dt.days.fillna(999).astype(int)
    df["days_since_created"] = (now - df["created_at"]).dt.days.fillna(999).astype(int)
    df["contact_speed"] = (df["contacted_at"] - df["created_at"]).dt.days.fillna(999).astype(int)
    df["notes_length"] = df["notes"].astype(str).str.len().fillna(0).astype(int)
    df["has_notes"] = df["notes"].astype(str).str.strip().ne("")
    df["created_day_of_week"] = df["created_at"].dt.dayofweek.fillna(-1).astype(int)
    df["created_month"] = df["created_at"].dt.month.fillna(-1).astype(int)

    if top_locations is None:
        top_locations = df["location"].value_counts().head(settings.top_n_locations).index.tolist()

    df["location_grouped"] = np.where(df["location"].isin(top_locations), df["location"], "Other")

    cat = pd.get_dummies(df[["source", "course_service", "location_grouped"]], prefix=["source", "course_service", "location"], dtype=int)
    num = df[[
        "gender_binary",
        "has_location",
        "has_phone",
        "has_referral",
        "referral_lead_count",
        "days_since_contacted",
        "days_since_created",
        "contact_speed",
        "notes_length",
        "has_notes",
        "created_day_of_week",
        "created_month",
    ]].astype(int)
    return pd.concat([num, cat], axis=1)


def build_training_matrix(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, LeadFeatureArtifacts]:
    top_locations = df.get("location", pd.Series(dtype=object)).fillna("Unknown").value_counts().head(settings.top_n_locations).index.tolist()
    X = add_engineered_features(df, top_locations=top_locations)
    y = (df.get("stage", pd.Series(dtype=object)).fillna("").str.lower() == "paid").astype(int)
    artifacts = LeadFeatureArtifacts(feature_columns=X.columns.tolist(), top_locations=top_locations)
    return X, y, artifacts
