#!/bin/bash

# Navigate to the repository directory
cd ~/piwrgb

# Optionally, activate a Python virtual environment if used
# source venv/bin/activate

# Get a random number using the Node.js script and store it in a variable
RANDOM_NUMBER=$(./get_random_number.js)

# Call the Python script with the flash command and the random number
sudo python3 flashy.py flash $RANDOM_NUMBER

