import json
import os

data_file = "pokemons.json"

def load_database():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {}

def save_database(db):
    with open(data_file, 'w') as f:
        json.dump(db, f, indent=4)
