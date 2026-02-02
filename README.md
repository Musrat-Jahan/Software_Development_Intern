# Software_Development_Intern

Hi, I am **Musrat**.
I am currently doing my placement in MetroBlue Tech Systems Ltd..
During this placement, I am learning software development, specifically programming language.

## Weekly Learning Progress

### Week 1 – Programming Fundamentals
In the first week, I learned the **basics of Python**, including:
-Python fundamentals
* Python syntax
* Variables and data types(List, Tuple, Set, Dictionary)
* Input and output
* Conditional statements (if / else)
* Control structures (loops)
* Functions and modules
  
  [Presenatation in Python ](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Python%20Slide.pptx)
  
### Week 2 – Simple Python Project
In the second week, I worked on a simple Python program:

* **Number Guessing Game**
* Used random numbers
* Took user input
* Applied conditions and loops

[Guess Game Python File](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Guess_Game.py)

## Smart Number Guessing Game – Explanation

This is a simple Python number guessing game where the computer generates a random secret number and the player tries to guess it within a limited number of attempts.

---
## How the Game Works

- The program asks the user if they want to start the game.
- The player selects a difficulty level:
  - **Easy**: Numbers between 1–10 with 5 attempts
  - **Hard**: Numbers between 1–50 with 3 attempts
- The computer randomly selects a secret number.
- The player enters guesses and receives feedback:
  - Too Low
  - Too High
  - Correct
- The game ends when the number is guessed or attempts run out.
- The player can choose to play multiple rounds.

---

## Program Structure

### `ask_yes_no()`
- Handles yes/no questions safely.
- Accepts only `yes/y` or `no/n`.
- Rejects invalid input.

### `choose_option()`
- Allows the user to select **Easy** or **Hard** mode.
- Returns the maximum number, attempts, and difficulty level.

### `play_game()`
- Generates the secret number.
- Takes and validates user guesses.
- Tracks remaining attempts.
- Displays game results.

### `main()`
- Controls the overall game flow.
- Starts the game and manages replay options.

---

