import random
from storage import load_database, save_database
from pokeapi import fetch_all_pokemon_names, fetch_pokemon_details
from display import display_pokemon

def main():
    db = load_database()

    while True:
        choice = input("would you like to draw a pokemon? (yes/no): ").strip().lower()
        if choice == "yes":
            all_names = fetch_all_pokemon_names()
            if not all_names:
                continue

            selected = random.choice(all_names)

            if selected in db:
                print("pokemon already in database.")
                display_pokemon(db[selected])
            else:
                print("fetching new pokemon data...")
                details = fetch_pokemon_details(selected)
                if details:
                    db[selected] = details
                    save_database(db)
                    display_pokemon(details)
                else:
                    print("failed to fetch details.")
        elif choice == "no":
            print("see you next time.")
            break
        else:
            print("please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
