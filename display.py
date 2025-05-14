def display_pokemon(pokemon):
    print("\n--- pokemon drawn ---")
    print(f"name: {pokemon['name'].title()}")
    print(f"base experience: {pokemon['base_experience']}")
    print(f"abilities: {', '.join(pokemon['abilities'])}")
    print("\n")
