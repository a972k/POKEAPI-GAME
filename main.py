import random
from storage import load_database, save_database
from pokeapi import fetch_all_pokemon_names, fetch_pokemon_details
from display import display_pokemon

# this is a simple Pokémon drawing game that fetches Pokémon data from the pokeapi.
def main():
    print("Welcome to the Pokémon Drawing Game!")
     # load the existing database or create a new one
    db = load_database()

    # main game loop
    while True:
        choice = input("would you like to draw a pokemon? (yes/no): ").strip().lower()
        if choice == "yes":
            all_names = fetch_all_pokemon_names()
            if not all_names:
                continue

            selected = random.choice(all_names)
            
            # check if the selected pokemon is already in the database if not fetch its details, or quit the game 
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
