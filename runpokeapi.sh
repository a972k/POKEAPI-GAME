#!/bin/bash

# Install dependencies
sudo apt update
sudo apt install -y git python3 python3-pip

# Clone the app from GitHub
git clone https://github.com/a972k/POKEAPI-GAME.git  

# Install Python dependencies (if any)
cd ~/pokeapp
pip3 install -r requirements.txt 2>/dev/null || true

# Add usage explanation on login
echo -e "\nWelcome to Pokémon Drawer App!" | sudo tee -a /etc/motd
echo "Run it using: python3 ~/pokeapp/main.py" | sudo tee -a /etc/motd

# Optional: test the app
python3 main.py <<EOF
no
EOF
