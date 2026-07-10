from types import SimpleNamespace

import app as app_module


def test_email_follow_up_gets_fallback_subject_when_ai_subject_is_empty(
    monkeypatch,
):
    monkeypatch.setattr(
        app_module,
        "get_org_profile",
        lambda: {"name": "Test Nonprofit"},
    )

    opportunity = SimpleNamespace(
        outreach_channel="email",
        recommended_target="Test Sponsor",
        parent_prospect="Parent Sponsor",
    )

    result = app_module.normalize_follow_up_draft(
        opportunity,
        {
            "subject": "   ",
            "message": "  Following up on our sponsorship request.  ",
        },
    )

    assert result["subject"] == (
        "Following up: Test Nonprofit and Test Sponsor"
    )
    assert result["message"] == (
        "Following up on our sponsorship request."
    )


def test_email_follow_up_preserves_ai_generated_subject(monkeypatch):
    monkeypatch.setattr(
        app_module,
        "get_org_profile",
        lambda: {"name": "Test Nonprofit"},
    )

    opportunity = SimpleNamespace(
        outreach_channel="email",
        recommended_target="Test Sponsor",
        parent_prospect="Parent Sponsor",
    )

    result = app_module.normalize_follow_up_draft(
        opportunity,
        {
            "subject": "  Quick sponsorship follow-up  ",
            "message": "  Could we schedule a short conversation?  ",
        },
    )

    assert result["subject"] == "Quick sponsorship follow-up"
    assert result["message"] == (
        "Could we schedule a short conversation?"
    )


def test_phone_follow_up_does_not_receive_email_subject(monkeypatch):
    monkeypatch.setattr(
        app_module,
        "get_org_profile",
        lambda: {"name": "Test Nonprofit"},
    )

    opportunity = SimpleNamespace(
        outreach_channel="phone",
        recommended_target="Test Sponsor",
        parent_prospect="Parent Sponsor",
    )

    result = app_module.normalize_follow_up_draft(
        opportunity,
        {
            "subject": "",
            "message": "  Phone follow-up script.  ",
        },
    )

    assert result["subject"] == ""
    assert result["message"] == "Phone follow-up script."
