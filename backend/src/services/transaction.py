import json
from pathlib import Path
from typing import List, Dict

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "transactions.json"

def load_transactions()-> List[Dict]:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"The data file not found at {DATA_PATH}!!")
    if DATA_PATH.stat().st_size == 0:
        return []
    with open(DATA_PATH, "r", encoding = "utf-8") as file:
        return json.load(file)
    
def get_all_transactions()->List[Dict]:      #It just use for call another function to make the code more clean
    return load_transactions()

def new_transaction(new_transactions: dict):
    data = load_transactions()
    data.insert(0, new_transactions)

    with open(DATA_PATH, "w", encoding = "utf-8") as file:
        json.dump(data, file, indent=4)

