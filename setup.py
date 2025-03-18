from setuptools import setup, find_packages

setup(
    name="car-racing-game",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pygame==2.5.2",
    ],
    author="fuzzypanworld",
    description="A simple 2D car racing game built with Python and Pygame",
    python_requires=">=3.6",
)