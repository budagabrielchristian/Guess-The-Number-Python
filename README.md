# README: Number Guessing Games

## Overview
This project contains two Python implementations of number guessing games:

1. **Random Number Guesser** - In this game, the computer generates a random number between 1 and 100, and the player (in this case, the computer itself) tries to guess the number.
2. **Binary Search Guesser** - This version optimizes the computer’s guessing strategy using a binary search algorithm, significantly reducing the number of attempts required to find the correct number.

## Table of Contents
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Descriptions](#game-descriptions)
  - [Random Number Guesser](#random-number-guesser)
  - [Binary Search Guesser](#binary-search-guesser)
- [How the Binary Search Works](#how-the-binary-search-works)
- [Customization](#customization)
- [Contributing](#contributing)

---

## Installation

### Requirements
- Python 3.x
- No external libraries are needed for these games as they use the standard Python library.

### Steps:
1. Clone the repository or download the Python files to your local machine.
   ```bash
   git clone https://github.com/budagabrielchristian/Guess-The-Number-Python.git
   ```
2. Navigate to the directory where the Python files are stored.
   ```bash
   cd Guess-The-Number-Python
   ```

---

## How to Run

You can run the Python scripts in your terminal or using any Python IDE.

To start the guessing game, execute either of the Python files:

1. **Random Number Guesser**:
   ```bash
   python main.py
   ```

2. **Binary Search Guesser**:
   ```bash
   python computer_playing.py
   ```

---

## Game Descriptions

### Random Number Guesser

In this game, the computer generates a random number between 1 and 100. The computer itself tries to guess the number using a basic mid-point calculation strategy that does not take advantage of optimization techniques like binary search.

- The game keeps track of the number of attempts the computer makes.
- It uses simple feedback loops to check whether the guess is too high, too low, or correct.
- The computer continues guessing until it correctly guesses the randomly generated number or the number of attempts reaches 100.

### Binary Search Guesser

This game improves the computer's guessing strategy using the **binary search algorithm**. The computer narrows the guessing range after each guess based on whether the current guess is too high or too low, thus reducing the number of guesses needed to find the correct number.

- The computer's first guess is the midpoint of the current range (initially 1 to 100).
- After each incorrect guess, the range is halved:
  - If the guess is too high, the upper bound (`current_max`) is reduced.
  - If the guess is too low, the lower bound (`current_min`) is increased.
- The game continues until the computer guesses the number correctly or reaches a limit of 100 attempts.

---

## How the Binary Search Works

Binary search is a highly efficient algorithm for finding a target number in a sorted range. In this game:
1. The computer guesses the middle number between the minimum and maximum of the range.
2. It receives feedback on whether the guess is higher or lower than the target number.
3. Depending on the feedback:
   - If the guess is too high, the computer reduces the upper bound to one less than the guess.
   - If the guess is too low, the computer increases the lower bound to one more than the guess.
4. This process continues, halving the search range with each step, until the correct number is found.

### Example:
1. The random number is 67.
2. The computer first guesses 50 (midpoint of 1 and 100).
3. Feedback: "Higher."
4. The new range becomes 51 to 100. The computer guesses the midpoint again (75).
5. Feedback: "Lower."
6. The new range becomes 51 to 74. The computer guesses 62.
7. Feedback: "Higher."
8. The process repeats until the computer guesses 67.

---

## Customization

You can modify the game by changing the range or adding new features.

### Changing the Range
If you want the computer to guess a number within a different range, simply update the `current_min` and `current_max` variables in both games:

```python
current_min = 1
current_max = 500  # Change the max range
```

### Adjusting Guessing Attempts
The maximum number of attempts is currently limited to 100. If you want to change this limit, you can update the condition in the `while` loop in both scripts.

---

## Contributing

Contributions are welcome! If you'd like to improve the project or add new features, please:
1. Fork the repository.
2. Make your changes in a new branch.
3. Submit a pull request explaining the changes.

--- 
