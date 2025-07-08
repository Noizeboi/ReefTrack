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
    if phosphate and phosphate > 0.1:
    if ammonia and ammonia > 0.25:
    if pH and pH < 7.9:
    if alk and ((mode == "SPS" and (alk < 7.5 or alk > 8.5)) or (mode == "LPS" and (alk < 7 or alk > 12))):
    if "Skimmer" in equipment:
    if "Heater" in equipment:
    if mode == "SPS":
    return suggestions
# Load dropdown models early
import json
try:
    with open("dropdown_models.json", "r") as f:
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
SAVE_FILE = "reef_data.json"
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)
# Load and Save
def load_tanks():
    if os.path.exists(SAVE_FILE):
    return {}
    with open(SAVE_FILE, "w") as f:
# Default modes
default_modes = {
    "Fish Only": {
    },
    "LPS": {
    },
    "SPS": {
    }
}
def check_alerts(params, mode):
    alerts = []
    for param, (low, high) in combined_modes.get(mode, {}).items():
    return alerts
def highlight_outliers(row, mode):
    styles = []
    for col in row.index:
    return styles
# Load tanks
# Sidebar
def get_default_tank_template():
    return {
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
    # Add + edit custom modes
# Main Interface
# Equipment Configuration - Safe, Form-Free Version
try:
    with open("dropdown_models.json", "r") as f:
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
        # Heater wattage check
        # Skimmer tank rating check
        # Return pump vs overflow flow
# Inject suggested maintenance into Overview and Maintenance Tabs