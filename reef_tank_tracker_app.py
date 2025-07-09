default_modes = {
    "Fish Only": {
        "Ammonia (ppm)": (0, 0.25),
        "Nitrite (ppm)": (0, 0.5),
        "Nitrate (ppm)": (0, 40),
        "Phosphate (ppm)": (0, 0.5)
    },
    "LPS": {
        "Calcium (ppm)": (380, 450),
        "Alkalinity (dKH)": (7.5, 8.5),
        "Magnesium (ppm)": (1200, 1400)
    },
    "SPS": {
        "Calcium (ppm)": (400, 450),
        "Alkalinity (dKH)": (8.0, 9.0),
        "Magnesium (ppm)": (1300, 1400)
    }
}
def suggest_maintenance(tank):
    suggestions = []
    mode = tank.get("mode", "Fish Only")
    equipment = tank.get("equipment", [])
    data = tank.get("data", [])
    maintenance = tank.get("maintenance", [])
    latest = data[-1] if data else {}
    get_val = lambda x: float(latest.get(x, 0)) if latest.get(x) not in [None, '', 'N/A'] else None
    nitrate = get_val("Nitrate (ppm)")
    phosphate = get_val("Phosphate (ppm)")
    ammonia = get_val("Ammonia (ppm)")
    pH = get_val("pH")
    alk = get_val("Alkalinity (dKH)")
    if nitrate and nitrate > 40:
        suggestions.append("Nitrate is high – perform 20–30% water change and clean filter media.")
    if phosphate and phosphate > 0.1:
        suggestions.append("Phosphate elevated – replace GFO or reduce feeding.")
    if ammonia and ammonia > 0.25:
        suggestions.append("Toxic ammonia detected – urgent water change recommended.")
    if pH and pH < 7.9:
        suggestions.append("Low pH – improve aeration or review CO₂ levels.")
    if alk and ((mode == "SPS" and (alk < 7.5 or alk > 8.5)) or (mode == "LPS" and (alk < 7 or alk > 12))):
        suggestions.append("Alkalinity instability – dose buffer or use auto-doser.")
    if "Skimmer" in equipment:
        from datetime import datetime
        now = datetime.now()
        clean_logs = [e for e in maintenance if "skimmer" in e.get("Task", "").lower()]
    if clean_logs:
        last_clean = max([datetime.strptime(e["Date"], "%Y-%m-%d") for e in clean_logs])
        days = (now - last_clean).days
        if days > 10:
            suggestions.append(f"Skimmer last cleaned {days} days ago – clean recommended.")
    else:
        suggestions.append("Skimmer installed but never cleaned – log a clean soon.")
    if clean_logs:
        last_clean = max([datetime.strptime(e["Date"], "%Y-%m-%d") for e in clean_logs])
        days = (now - last_clean).days
        if days > 10:
            suggestions.append(f"Skimmer last cleaned {days} days ago – clean recommended.")
    else:
        suggestions.append("Skimmer installed but never cleaned – log a clean soon.")
    if "Heater" in equipment:
        suggestions.append("Check heater calibration monthly to avoid temperature drift.")
    if mode == "SPS":
        suggestions.append("SPS coral requires stable parameters – test calcium, alk, mag regularly.")
    return suggestions
import streamlit as st
# Load dropdown models early
import json
try:
    with open("dropdown_models.json", "r") as f:
        dropdown_models = json.load(f)
except FileNotFoundError:
    dropdown_models = {}
def main():
    st.error("Missing dropdown_models.json – please check your repository.")
    import pandas as pd
    import os
    from datetime import datetime
    import matplotlib.pyplot as plt
    # Initialize session state
    defaults = {
    "selected_tank": None,
    "tanks": {},
}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    st.session_state[key] = value
    SAVE_FILE = "reef_data.json"
    IMAGE_DIR = "images"
    os.makedirs(IMAGE_DIR, exist_ok=True)
    # Load and Save
def load_tanks():
    pass  # placeholder body
def save_tanks():
    pass
def save_tanks():
    with open(SAVE_FILE, "w") as f:
        json.dump(st.session_state.tanks, f)
    json.dump({
    "tanks": st.session_state.tanks,
    "custom_modes": st.session_state.custom_modes
    }, f, indent=2, default=str)
    # Default modes
default_modes = {
    },
