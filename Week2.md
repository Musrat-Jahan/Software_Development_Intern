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


---
