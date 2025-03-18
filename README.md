# 2D Car Racing Game

A simple 2D car racing game built with Python and Pygame. Dodge the obstacles and try to get the highest score!

## Prerequisites

- Python 3.6 or higher
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/fuzzypanworld/mcp-project-2024.git
cd mcp-project-2024
```

2. Set up the virtual environment:

### Windows
```bash
# Run the setup script
setup_venv.bat

# Activate the virtual environment (if not already activated)
venv\Scripts\activate
```

### Linux/macOS
```bash
# Make the setup script executable
chmod +x setup_venv.sh

# Run the setup script
./setup_venv.sh

# Activate the virtual environment (if not already activated)
source venv/bin/activate
```

The setup scripts will:
- Create a virtual environment
- Activate it
- Install all required dependencies
- Set up the project for development

## How to Play

1. Make sure the virtual environment is activated (you should see `(venv)` in your terminal)

2. Run the game:
```bash
python car_racing.py
```

3. Game Controls:
- Use LEFT ARROW key to move left
- Use RIGHT ARROW key to move right
- Press SPACE to restart after game over

4. Game Rules:
- Avoid the green obstacles
- Each obstacle you successfully dodge adds to your score
- Hitting an obstacle ends the game

## Features

- Simple and intuitive controls
- Increasing difficulty as you progress
- Score tracking
- Smooth animations
- Game over and restart functionality

## Development

The project uses a virtual environment to manage dependencies. If you want to add new dependencies:

1. Activate the virtual environment
2. Install new packages using pip
3. Update `setup.py` with the new dependencies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.