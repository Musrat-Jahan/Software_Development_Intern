# Software_Development_Intern

Hi, I am **Musrat**.
I am currently doing my placement in MetroBlue Tech Systems Ltd..
During this placement, I am learning software development, specifically programming language.

## Weekly Learning Progress

### Week 1 
### Task_1– Programming Fundamentals
In the first week, I learned the **basics of Python**, including:
-Python fundamentals
* Python syntax
* Variables and data types(List, Tuple, Set, Dictionary)
* Input and output
* Conditional statements (if / else)
* Control structures (loops)
* Functions and modules


Python Data Types**

**Built-in Data Types:**

* `int` → Integer numbers: `10, -5, 0`
* `float` → Decimal numbers: `3.14, 0.5`
* `str` → Strings: `"Hello", 'Python'`
* `bool` → Boolean: `True, False`
* `list` → Ordered, mutable: `[1,2,3]`
* `tuple` → Ordered, immutable: `(1,2,3)`
* `dict` → Key-value pairs: `{"name":"Alice", "age":25}`
* `set` → Unordered, unique: `{1,2,3}`

Type Checking

x = 10
print(type(x))  # <class 'int'>

y = [1, 2, 3]
print(type(y))  # <class 'list'>

Type Casting & Conversion

* **Int → Float**: `float(10) → 10.0`
* **Float → Int**: `int(3.99) → 3`
* **String → Int**: `int("50") → 50`
* **Int → String**: `str(50) → "50"`

**Implicit vs Explicit Casting:**


# Implicit
x = 5 + 2.5  =  7.5 (int + float → float)

# Explicit
y = int("100")  # 100

Arithmetic Operators

| Operator | Example  | Result |
| -------- | -------- | ------ |
| `+`      | `5 + 3`  | 8      |
| `-`      | `5 - 3`  | 2      |
| `*`      | `5 * 3`  | 15     |
| `/`      | `5 / 2`  | 2.5    |
| `//`     | `5 // 2` | 2      |
| `%`      | `5 % 2`  | 1      |
| `**`     | `2 ** 3` | 8      |

 Comparison Operators

| Operator | Meaning       | Example          |
| -------- | ------------- | ---------------- |
| `==`     | Equal         | `5 == 5 → True`  |
| `!=`     | Not equal     | `5 != 3 → True`  |
| `>`      | Greater than  | `5 > 3 → True`   |
| `<`      | Less than     | `5 < 3 → False`  |
| `>=`     | Greater/equal | `5 >= 5 → True`  |
| `<=`     | Less/equal    | `5 <= 3 → False` |


 Logical Operators

| Operator | Meaning           | Example                  |
| -------- | ----------------- | ------------------------ |
| `and`    | True if both True | `True and False → False` |
| `or`     | True if any True  | `True or False → True`   |
| `not`    | Negation          | `not True → False`       |


Assignment Operators

x = 10

x += 5  ,  x = 15

x -= 3  ,  x = 12

x *= 2  , x = 24

x /= 4  ,  x = 6.0

x **= 2 ,  x = 36.0


 Identity & Membership Operators

**Identity Operators:**

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)    # True
print(a is c)    # False


**Membership Operators:**
fruits = ["apple","banana"]
print("apple" in fruits)       # True
print("mango" not in fruits)   # True

 Summary**

* Python has **multiple data types**: int, float, str, bool, list, tuple, dict, set
* Use **type()** to check variable type
* **Casting**: implicit (automatic) vs explicit (manual)
* **Operators** help perform arithmetic, comparisons, logic, assignment, and membership checks
* **Identity & membership operators** help compare objects and check elements

---

### Task 2 – Simple Python Project
In the second week, I worked on a simple Python program:

* **Number Guessing Game**
* Used random numbers
* Took user input
* Applied conditions and loops

[Guess Game Python File](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Guess_Game.py)

## Smart Number Guessing Game – Explanation

This is a simple Python number guessing game where the computer generates a random secret number and the player tries to guess it within a limited number of attempts.

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
## Week 2
## Task 1: Personal Expense

[Guess Game Python File](https://github.com/Musrat-Jahan/Software_Development_Intern/blob/main/Personal%20Expense%20Tracker.py))
Application Type
* Must be a **console / terminal program** (not GUI, not web).
* Must show a **menu** and let the user select options.
* Must keep running until the user chooses **Exit**.

*Features* 

*Add a New Expense*

When user chooses “Add Expense”, program must ask for:
* **Amount spent** (number: int/float)
* **Category** (choose from fixed list)
* **Description** (short text like “Lunch”)
* **Date** (string like `YYYY-MM-DD` or another consistent format)
After input, the expense must be saved into the program’s expense list.

*View All Expenses*

When user chooses “View Expenses”:
* Show every stored expense clearly.
* Each expense display must include:
  * Amount
  * Category
  * Description
  * Date
* Display must be readable (one line per expense is fine).

*View Expense Summary*

When user chooses “View Summary”, program must show:
 **Total amount spent**
   * Sum of all expense amounts.
 **Average spending**
   * Total amount spent ÷ number of expenses.
   * Must handle case when there are **0 expenses** (avoid divide-by-zero error).
 **Total spent per category**
   * Show category totals like:
     * Food: $xx
     * Transport: $xx
     * Bills: $xx
     * Shopping: $xx
     * Others: $xx
  *Save Expenses to a File*

* Expenses must not disappear when program closes.
* Program must save all expenses into a file when user chooses “Save and Exit” (or separately if you add a “Save” option).
* File format can be text, CSV, or JSON. Any is acceptable as long as it works.

*Load Expenses from a File*

* When program starts, it must load saved expenses automatically.
* After loading, previously saved expenses must be available for:
  * View Expenses
  * View Summary

#### Python Concepts 

   1. Lists
* Use a **list** to store all expenses.
* Example requirement: `expenses = [ ... ]` containing expense records.
  
 2. Tuples
* Use a **tuple** for fixed categories (cannot change during runtime).
* Must include categories like:
  * Food
  * Transport
  * Bills
  * Shopping
  * Others
* The program should only allow categories from that tuple.

 3. Dictionaries
* Each single expense must be stored as a **dictionary** with these keys:
  * `"amount"`
  * `"category"`
  * `"description"`
  * `"date"`

4. Sets
* Must use a **set somewhere meaningful**.
* Examples:
  * Track **unique categories used**
  * Track **unique dates**
* The set should come from your expenses list.

 5. Functions
Minimum recommended functions:
* Add expense
* View expenses
* Calculate summary totals
* Save to file
* Load from file
Avoid writing everything inside one big loop.

6. Loops
Must use loops for:
* The **menu** (keeps program running)
* Iterating over expenses list to display expenses and calculate summary

7. Conditional Statements
Must use `if / elif / else` for:
* Handling menu choices
* Checking valid input
* Summary calculations (like if no expenses)

 8. User Input & Type Conversion
* Must use `input()` for user interaction.
* Must convert:
  * Amount to `float` or `int`
  * Menu choices to `int` if you want numeric menu
* Must validate user inputs reasonably.

 9. Error Handling
Must use `try / except` to handle:
* User enters text instead of number for amount
* User enters invalid menu option
* Any input conversion errors (ValueError)

 10. File Handling
Must use:
* `open()`
* `read()` / `write()` (or `readlines()`)
* Load and save expense data to/from a file.

Program Flow Requirement (Menu):
menu should look like this (or similar):
1. Add Expense
2. View Expenses
3. View Summary
4. Save and Exit
And it must:
* Keep showing until Exit is chosen.
* Not crash on wrong input.


#### Optional (Not Mandatory)

Only if you finish early:
* Monthly budget limit
* Export to CSV
* Refactor into class-based version



