# Pokémon Guessing Game

- This is a simple game where the player has to guess the name of a Pokémon displayed with its letters scrambled. 
- The player has a limited number of attempts to guess the correct name. 
- The game randomly selects a Pokémon name from the Pokédex API and scrambles the letters for display.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running the following command:

> pip install requests

## Usage

1. Run the script `pokemon_guess.py` using Python.
2. The game will display a scrambled Pokémon name and prompt the player to enter their guess.
3. Enter your guess and press Enter.
4. If the guess is correct, the game will display a success message and end.
5. If the guess is incorrect, the game will display an error message and give the player another attempt.
6. The player has a total of 3 attempts to guess the correct name.
7. After the maximum number of attempts is reached, the game will display the correct Pokémon name.

## Dependencies

- requests: This library is used to make HTTP requests to the Pokédex API.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

