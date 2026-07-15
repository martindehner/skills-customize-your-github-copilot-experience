
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game to practice core Python programming concepts such as loops, conditionals, string handling, and user input. By the end of this assignment, you will create a complete terminal-based game with clear game flow and win/lose outcomes.

## 📝 Tasks

### 🛠️ Set Up the Hangman Game Loop

#### Description
Create the main game structure for Hangman. Select a random word from a predefined list, collect user guesses one letter at a time, and keep the game running until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Define a list of possible words and randomly choose one word at the start of the game.
- Ask the player for one letter guess per turn using `input()`.
- Reject invalid input (such as empty input, numbers, symbols, or multiple letters) and ask again.
- End the game when the player has guessed the full word or used all allowed incorrect guesses.

### 🛠️ Display Progress and Final Result

#### Description
Show the player useful feedback during each turn. Reveal correctly guessed letters in the word, track incorrect guesses remaining, and display a clear final message when the game ends.

#### Requirements
Completed program should:

- Display the hidden word with unguessed letters shown as `_` (for example, `_ _ n g m a n`).
- Keep track of guessed letters so repeated guesses can be handled clearly.
- Decrease remaining attempts only when a guess is incorrect.
- Print a win message when the word is fully guessed and a lose message that reveals the correct word when attempts reach zero.
