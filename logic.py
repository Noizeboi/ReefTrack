def suggest_maintenance(tank):
    suggestions = []

    mode = tank.get("mode", "Fish Only")
    equipment = tank.get("equipment", [])
    data = tank.get("data", [])
    maintenance = tank.get("maintenance", [])

    latest = data[-1] if data else {}

    def get_val(x):
        raw = latest.get(x)
        return float(raw) if raw not in [None, "", "N/A"] else None

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
        suggestions.append("Low pH – improve aeration or review CO₂ buildup.")
    if alk and ((mode == "SPS" and (alk < 7.5 or alk > 8.5)) or (mode == "LPS" and (alk < 7 or alk > 12))):
        suggestions.append("Alkalinity is out of optimal range – verify dosing or buffer system.")

    if "Skimmer" in equipment:
        last_cleaned = next((m for m in reversed(maintenance) if m.get("type") == "Skimmer"), None)
        if last_cleaned:
            days = (datetime.now() - datetime.strptime(last_cleaned["date"], "%Y-%m-%d")).days
            if days > 10:
                suggestions.append(f"Skimmer last cleaned {days} days ago – clean recommended.")
        else:
            suggestions.append("Skimmer installed but never cleaned – log a clean soon.")

    if "Heater" in equipment:
        suggestions.append("Check heater calibration monthly to avoid temperature drift.")
    if mode == "SPS":
        suggestions.append("SPS coral requires stable parameters – test calcium, alk, mag regularly.")

    return suggestions