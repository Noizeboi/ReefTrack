import pytest
from logic import suggest_maintenance

def test_high_nitrate():
    tank = {
        "mode": "Fish Only",
        "equipment": [],
        "data": [{"Nitrate (ppm)": "50"}],
        "maintenance": []
    }
    suggestions = suggest_maintenance(tank)
    assert any("Nitrate is high" in s for s in suggestions)

def test_low_ph():
    tank = {
        "mode": "Fish Only",
        "equipment": [],
        "data": [{"pH": "7.6"}],
        "maintenance": []
    }
    suggestions = suggest_maintenance(tank)
    assert any("Low pH" in s for s in suggestions)

def test_skimmer_needs_cleaning():
    from datetime import datetime, timedelta
    past_date = (datetime.now() - timedelta(days=11)).strftime("%Y-%m-%d")
    tank = {
        "mode": "Fish Only",
        "equipment": ["Skimmer"],
        "data": [{}],
        "maintenance": [{"Date": past_date, "Task": "Clean skimmer"}]
    }
    suggestions = suggest_maintenance(tank)
    assert any("Skimmer last cleaned" in s for s in suggestions)

def test_no_data_defaults():
    tank = {
        "mode": "Fish Only",
        "equipment": ["Heater"],
        "data": [],
        "maintenance": []
    }
    suggestions = suggest_maintenance(tank)
    assert "Check heater calibration" in " ".join(suggestions)
