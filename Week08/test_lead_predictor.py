from app.lead_scoring.predict import score_lead


def test_score_lead_returns_expected_keys():
    result = score_lead({
        "source": "Facebook",
        "course_service": "IELTS",
        "gender": "Male",
        "location": "Darwin",
        "phone": "0400000000",
        "referral_id": 1,
        "notes": "Very interested and ready to pay soon"
    })
    assert "score" in result
    assert "label" in result
    assert "factors" in result
    assert 0.0 <= result["score"] <= 1.0
