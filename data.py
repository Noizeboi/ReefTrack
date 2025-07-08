import json

try:
    with open("dropdown_models.json", "r") as f:
        dropdown_models = json.load(f)
except FileNotFoundError:
    dropdown_models = {}