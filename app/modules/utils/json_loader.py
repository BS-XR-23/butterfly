import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "public" / "data" / "products.json"


def load_products():
    with open(DATA_PATH, "r") as f:
        return json.load(f)