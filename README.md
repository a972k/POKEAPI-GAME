# POKEAPI-GAME
a python based game using pokeAPI 
This is a simple CLI-based Pokémon drawing game that fetches data from [PokeAPI](https://pokeapi.co/) and stores it locally. This version is designed for **automatic deployment on AWS EC2 via CloudFormation**.

* Features

- Fetch random pokemon data from PokeAPI
- Save drawn pokemon to a JSON file
- Auto-starts on SSH login
- Includes bash message explaining the game
- Fully deployable via aws cloudFormation

* Requirements

- An aws account
- An existing EC2 Key Pair (for SSH)
- AWS CLI installed locally

* Deployment via aws cloudFormation

1. Clone this repo to your local machine.
2. Use the provided cloudFormation template to create your EC2 stack.

* Example CLI deployment:

#bash
#aws cloudformation create-stack \
# --stack-name pokemon-game-stack \
# --template-body file://pokemon-template.yaml \
# --parameters ParameterKey=KeyName,ParameterValue=your-key-name

thank you, and goodbye. 
