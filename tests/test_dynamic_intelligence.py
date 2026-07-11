import app as app_module


def test_workspace_uses_database_backed_intelligence():
    source = open("app.py", encoding="utf-8").read()

    assert "seed_sponsorship_intelligence(organization, initiative)" in source
    assert (
        "categories=get_sponsor_categories(organization, initiative)"
        in source
    )
    assert (
        "assets=get_sponsorship_assets(organization, initiative)"
        in source
    )


def test_dynamic_models_exist():
    source = open("app.py", encoding="utf-8").read()

    assert "class SponsorCategory(db.Model):" in source
    assert "class SponsorshipAsset(db.Model):" in source

    assert "organization_id" in source
    assert "initiative_id" in source


def test_seed_function_exists():
    source = open("app.py", encoding="utf-8").read()

    assert "def seed_sponsorship_intelligence(" in source
    assert "SponsorCategory.query.filter_by(" in source
    assert "SponsorshipAsset.query.filter_by(" in source
