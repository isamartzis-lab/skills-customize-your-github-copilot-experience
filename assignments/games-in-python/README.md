
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python that uses strings, loops, conditionals, and user input. By completing this assignment, you will practice managing game state and writing logic for win/lose outcomes.

## 📝 Tasks

### 🛠️ Set Up The Hidden Word

#### Description
Create the game setup by defining a list of possible words and selecting one word at random for each game.

#### Requirements
Completed program should:

- Store multiple possible words in a predefined list.
- Randomly choose one word from that list when the game starts.
- Initialize a display of the hidden word using underscores (for example: `_ _ _ _ _`).

### 🛠️ Build The Guessing Loop

#### Description
Implement the main game loop where the player guesses one letter at a time, the word display is updated, and incorrect guesses reduce the remaining attempts.

#### Requirements
Completed program should:

- Prompt the player to enter a letter guess.
- Reveal correctly guessed letters in their correct positions.
- Decrease remaining attempts for incorrect guesses.
- Show the current word progress and attempts remaining after each guess.
- End the game when the full word is guessed or attempts run out.
- Display a clear win message when the player guesses the word.
- Display a clear lose message and reveal the word when attempts are exhausted.

Example gameplay:

```text
Word: _ _ _ _
Attempts left: 6
Guess a letter: a
Word: _ a _ _
Attempts left: 6
```
