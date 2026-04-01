from __future__ import annotations

import pandas as pd

TOP_N_LOCATIONS = 10


def normalize_text_series(series: pd.Series, unknown: str = "unknown") -> pd.Series:
    return series.fillna(unknown).astype(str).str.strip().str.lower()


def create_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["converted"] = (normalize_text_series(df["stage"]) == "paid").astype(int)
    return df


def add_basic_boolean_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["has_location"] = df["location"].notna().astype(int)
    df["has_phone"] = df["phone"].notna().astype(int)
    df["has_referral"] = df["referral_id"].notna().astype(int)
    df["has_notes"] = df["notes"].notna().astype(int)
    return df


def add_referral_lead_count(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    referral_counts = df.groupby("referral_id")["id"].count().to_dict()
    df["referral_lead_count"] = df["referral_id"].map(referral_counts).fillna(0).astype(int)
    return df


def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    now = pd.Timestamp.now()

    for col in ["contacted_at", "created_at"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    df["days_since_contacted"] = (now - df["contacted_at"]).dt.days
    df["days_since_created"] = (now - df["created_at"]).dt.days
    df["contact_speed"] = (df["contacted_at"] - df["created_at"]).dt.days
    df["created_day_of_week"] = df["created_at"].dt.dayofweek + 1
    df["created_month"] = df["created_at"].dt.month

    for col in [
        "days_since_contacted",
        "days_since_created",
        "contact_speed",
        "created_day_of_week",
        "created_month",
    ]:
        df[col] = df[col].fillna(-1)
    return df


def add_notes_length(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["notes_length"] = df["notes"].fillna("").astype(str).str.len()
    return df


def encode_gender(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    gender_clean = normalize_text_series(df["gender"])
    df["gender_male"] = (gender_clean == "male").astype(int)
    df["gender_female"] = (gender_clean == "female").astype(int)
    df["gender_unknown"] = (~gender_clean.isin(["male", "female"])).astype(int)
    return df


def encode_source(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    source_dummies = pd.get_dummies(normalize_text_series(df["source"]), prefix="source")
    return pd.concat([df, source_dummies], axis=1)


def encode_course_service(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    service_dummies = pd.get_dummies(normalize_text_series(df["course_service"]), prefix="course_service")
    return pd.concat([df, service_dummies], axis=1)


def encode_top_locations(df: pd.DataFrame, top_n: int = TOP_N_LOCATIONS) -> pd.DataFrame:
    df = df.copy()
    location_clean = normalize_text_series(df["location"])
    top_locations = location_clean.value_counts().head(top_n).index.tolist()
    grouped = location_clean.apply(lambda x: x if x in top_locations else "other")
    location_dummies = pd.get_dummies(grouped, prefix="location")
    return pd.concat([df, location_dummies], axis=1)


def build_feature_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = create_target(df)
    df = add_basic_boolean_features(df)
    df = add_referral_lead_count(df)
    df = add_date_features(df)
    df = add_notes_length(df)
    df = encode_gender(df)
    df = encode_source(df)
    df = encode_course_service(df)
    df = encode_top_locations(df)
    return df


def select_model_features(df: pd.DataFrame) -> pd.DataFrame:
    base_features = [
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
        "gender_male",
        "gender_female",
        "gender_unknown",
    ]
    encoded_features = [
        col for col in df.columns
        if col.startswith("source_")
        or col.startswith("course_service_")
        or col.startswith("location_")
    ]
    feature_columns = base_features + encoded_features + ["converted"]
    return df[feature_columns].copy()


def build_single_prediction_row(payload: dict, training_columns: list[str]) -> pd.DataFrame:
    raw = pd.DataFrame([
        {
            "id": payload.get("id", 0),
            "source": payload.get("source"),
            "course_service": payload.get("course_service"),
            "gender": payload.get("gender"),
            "location": payload.get("location"),
            "phone": payload.get("phone"),
            "stage": payload.get("stage", "unknown"),
            "contacted_at": payload.get("contacted_at"),
            "created_at": payload.get("created_at"),
            "referral_id": payload.get("referral_id"),
            "notes": payload.get("notes"),
        }
    ])
    featured = build_feature_dataset(raw)
    featured = select_model_features(featured)
    if "converted" in featured.columns:
        featured = featured.drop(columns=["converted"])
    featured = featured.reindex(columns=training_columns, fill_value=0)
    return featured
