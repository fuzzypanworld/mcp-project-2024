#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install -e .

echo "Setup complete! You can now run the game using: python car_racing.py"
echo "To activate the virtual environment in the future, run: source venv/bin/activate"