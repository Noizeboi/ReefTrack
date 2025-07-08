def suggest_maintenance(tank):
    suggestions = []
    mode = tank.get("mode", "Fish Only")
    equipment = tank.get("equipment", [])
    data = tank.get("data", [])
    maintenance = tank.get("maintenance", [])
    latest = data[-1] if data else {}
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
    if "Heater" in equipment:
        suggestions.append("Check heater calibration monthly to avoid temperature drift.")
    if mode == "SPS":
        suggestions.append("SPS coral requires stable parameters – test calcium, alk, mag regularly.")
    return suggestions
# Load dropdown models early
import json
try:
    with open("dropdown_models.json", "r") as f:
        dropdown_models = json.load(f)
except FileNotFoundError:
    dropdown_models = {}
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
# Initialize session state
defaults = {
    "selected_tank": None,
    "tanks": {},
    "custom_modes": {}
}
for key, value in defaults.items():
SAVE_FILE = "reef_data.json"
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)
# Load and Save
def load_tanks():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            tanks = data.get("tanks", {})
            for t in tanks.values():
                img = t.get("profile_image")
                if isinstance(img, str) and not os.path.exists(os.path.join(IMAGE_DIR, img)):
                    t["profile_image"] = None
            return tanks
    return {}
def save_tanks():
    with open(SAVE_FILE, "w") as f:
        json.dump({
        }, f, indent=2, default=str)
# Default modes
default_modes = {
    "Fish Only": {
        "Temperature (°C)": (24, 27),
        "Salinity (SG)": (1.020, 1.026),
        "pH": (7.8, 8.4),
        "Ammonia (ppm)": (0, 0.25),
        "Nitrite (ppm)": (0, 0.5),
        "Nitrate (ppm)": (0, 40)
    },
    "LPS": {
        "Temperature (°C)": (24, 26),
        "Salinity (SG)": (1.024, 1.026),
        "pH": (8.0, 8.4),
        "Ammonia (ppm)": (0, 0),
        "Nitrite (ppm)": (0, 0),
        "Nitrate (ppm)": (0, 20),
        "Phosphate (ppm)": (0, 0.1),
        "Calcium (ppm)": (380, 450),
        "Alkalinity (dKH)": (7, 12),
        "Magnesium (ppm)": (1200, 1400)
    },
    "SPS": {
        "Temperature (°C)": (25, 26),
        "Salinity (SG)": (1.025, 1.026),
        "pH": (8.1, 8.4),
        "Ammonia (ppm)": (0, 0),
        "Nitrite (ppm)": (0, 0),
        "Nitrate (ppm)": (0, 5),
        "Phosphate (ppm)": (0, 0.03),
        "Calcium (ppm)": (400, 450),
        "Alkalinity (dKH)": (7.5, 8.5),
        "Magnesium (ppm)": (1300, 1400)
    }
}
def check_alerts(params, mode):
    alerts = []
    for param, (low, high) in combined_modes.get(mode, {}).items():
        try:
            val = float(params.get(param, 'N/A'))
            if val < low or val > high:
                alerts.append(f"{param}: {val} (Expected: {low}-{high})")
        except:
            continue
    return alerts
def highlight_outliers(row, mode):
    styles = []
    for col in row.index:
        if col in combined_modes[mode]:
            val = row[col]
            low, high = combined_modes[mode][col]
            if pd.notnull(val) and (val < low or val > high):
                styles.append("background-color: #ffcccc")
            else:
                styles.append("")
        else:
            styles.append("")
    return styles
# Load tanks
# Sidebar
            "display_capacity": None,
            "sump_capacity": None,
            "theme": "",
            "livestock": "",
            "equipment": [],
            "profile_image": None,
            "mode": "Fish Only",
            "data": [],
            "maintenance": [],
            "diary": []
        }
        save_tanks()
    # Add + edit custom modes
            save_tanks()
            updated = {}
                with col1:
                with col2:
                with col3:
                with col4:
                if not remove:
                    updated[param] = (new_low, new_high)
                save_tanks()
                save_tanks()
# Main Interface
# Equipment Configuration - Safe, Form-Free Version
try:
    with open("dropdown_models.json", "r") as f:
        dropdown_models = json.load(f)
except Exception:
    dropdown_models = {}
equipment_options = {
    "Heater": dropdown_models.get("Heaters", []),
    "LED Light": dropdown_models.get("LED Lights", []),
    "Skimmer": dropdown_models.get("Skimmers", []),
    "ATO System": dropdown_models.get("ATO Systems", []),
    "Return Pump": dropdown_models.get("Return Pumps", []),
    "Overflow Type": dropdown_models.get("Overflows", []),
}
    tank["selected_equipment"] = tank.get("selected_equipment", {})
    updated = False
    for eq_type, options in equipment_options.items():
        current = tank["selected_equipment"].get(eq_type)
        index = options.index(current) if current in options else 0 if options else 0
            f"{eq_type} Model",
            options,
            index=index,
            key=f"{eq_type}_select"
        )
        if selected != current:
            tank["selected_equipment"][eq_type] = selected
            updated = True
        if updated:
        else:
        validation_notes = []
        display_vol = tank.get("display_capacity", 0.0)
        sump_vol = tank.get("sump_capacity", 0.0)
        total_volume = display_vol + sump_vol
        from json import load as json_load
        with open("equipment_model_lookup.json", "r") as ef:
            model_lookup = json_load(ef)
        # Heater wattage check
        heater = tank["selected_equipment"].get("Heater")
        if heater in model_lookup:
            wattage = model_lookup[heater].get("wattage")
            if wattage and (total_volume / wattage > 3):  # Rough guide: 1W per 3L
                validation_notes.append(f"Heater '{heater}' may be underpowered for {total_volume}L.")
        # Skimmer tank rating check
        skimmer = tank["selected_equipment"].get("Skimmer")
        if skimmer in model_lookup:
            rated = model_lookup[skimmer].get("rated_tank_l")
            if rated and rated < total_volume:
                validation_notes.append(f"Skimmer '{skimmer}' is rated for {rated}L, which is under your tank volume.")
        # Return pump vs overflow flow
        pump = tank["selected_equipment"].get("Return Pump")
        overflow = tank["selected_equipment"].get("Overflow Type")
        if pump in model_lookup and overflow in model_lookup:
            pump_flow = model_lookup[pump].get("flow_lph")
            overflow_limit = model_lookup[overflow].get("recommended_flow_lph")
            if pump_flow and overflow_limit and pump_flow > overflow_limit:
                validation_notes.append(f"Pump '{pump}' may exceed overflow capacity '{overflow}' ({overflow_limit} L/h).")
        if validation_notes:
            for note in validation_notes:
                if profile_pic:
                    with open(os.path.join(IMAGE_DIR, filename), "wb") as f:
                        f.write(profile_pic.read())
                    tank["profile_image"] = filename
                save_tanks()
# Inject suggested maintenance into Overview and Maintenance Tabs