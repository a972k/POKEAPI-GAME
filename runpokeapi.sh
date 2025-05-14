#!/bin/bash

# Install dependencies
sudo apt update
sudo apt install -y git python3 python3-pip

# Clone the app from GitHub
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git ~/pokeapp

# Install Python dependencies (if any)
cd ~/pokeapp
pip3 install -r requirements.txt 2>/dev/null || true

# Add usage explanation on login
echo -e "\nWelcome to Pokémon Drawer App!" | sudo tee -a /etc/motd
echo "Run it using: python3 ~/pokeapp/poke_drawer.py" | sudo tee -a /etc/motd

# Optional: test the app
python3 poke_drawer.py <<EOF
no
EOF
