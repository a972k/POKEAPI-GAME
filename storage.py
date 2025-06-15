import json
import os

data_file = "pokemons.json"

# define function to load data. If the file does not exist, return an empty dictionary.
def load_database():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {}

# define function to save data to the database. If the file does not exist, it will be created.
def save_database(db):
    with open(data_file, 'w') as f:
        json.dump(db, f, indent=4)
