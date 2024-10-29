# Spaceman

**Spaceman** is a word-guessing game written in Python, similar to "Hangman." The player attempts to guess a secret word by guessing one letter at a time, with a limited number of incorrect guesses allowed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Gameplay](#gameplay)
- [Future Enhancements](#future-enhancements)

## Installation

1. **Clone the Repository**: Download or clone the repository from GitHub.
   ```bash
   git clone https://github.com/your-username/Spaceman.git
   cd Spaceman
   ```

2. **Dependencies**: Ensure you have Python 3 installed on your system.

## Usage

1. Ensure `words.txt` is in the same directory as `spaceman.py`.
2. Run the program by executing:
   ```bash
   python3 spaceman.py
   ```
3. Follow the prompts to play the game.

## File Overview

- **spaceman.py**: The main program file that contains the game logic. It loads a random word from `words.txt`, handles user input, checks guesses, and manages the game flow.
- **words.txt**: Contains a list of words separated by spaces, from which the program selects a secret word for each game.

## Gameplay

- You have **7 tries** to guess the secret word.
- Each turn, input a single letter as your guess.
- If the guessed letter is correct, it is revealed in the word. If not, you lose one of your available tries.
- The game continues until you either guess the entire word or run out of tries.
- After each game, you’ll be asked if you want to play again.

## STRETCH CHALLENGES

- Adding difficulty levels by adjusting the word length or the number of tries.
- Improving the `words.txt` file by including a more extensive vocabulary or by sourcing words based on themes.
- Allowing players to select categories or themes for the word list.

