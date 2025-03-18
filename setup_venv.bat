@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -e .

echo Setup complete! You can now run the game using: python car_racing.py
echo To activate the virtual environment in the future, run: venv\Scripts\activate.bat