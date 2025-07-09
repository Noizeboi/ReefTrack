from typing import Dict, Any, List

# Constants for threshold values
NITRATE_THRESHOLD = 40.0
PHOSPHATE_THRESHOLD = 0.1
AMMONIA_THRESHOLD = 0.25
PH_THRESHOLD = 7.9

def safe_float(val: Any) -> float | None:
    try:
        return float(val)
    except (ValueError, TypeError):
        return None

def suggest_maintenance(tank: Dict[str, Any]) -> List[str]:
    suggestions = []
    mode = tank.get("mode", "Fish Only")
    equipment = tank.get("equipment", [])
    data = tank.get("data", [])
    maintenance = tank.get("maintenance", [])

    latest = data[-1] if data else {}

    nitrate = safe_float(latest.get("Nitrate (ppm)"))
    phosphate = safe_float(latest.get("Phosphate (ppm)"))
    ammonia = safe_float(latest.get("Ammonia (ppm)"))
    pH = safe_float(latest.get("pH"))
    alk = safe_float(latest.get("Alkalinity (dKH)"))

    if nitrate is not None and nitrate > NITRATE_THRESHOLD:
        suggestions.append("Nitrate is high – perform 20–30% water change and clean filter media.")
    if phosphate is not None and phosphate > PHOSPHATE_THRESHOLD:
        suggestions.append("Phosphate elevated – replace GFO or reduce feeding.")
    if ammonia is not None and ammonia > AMMONIA_THRESHOLD:
        suggestions.append("Toxic ammonia detected – urgent water change recommended.")
    if pH is not None and pH < PH_THRESHOLD:
        suggestions.append("Low pH – improve aeration or review CO₂ levels.")

    return suggestions
