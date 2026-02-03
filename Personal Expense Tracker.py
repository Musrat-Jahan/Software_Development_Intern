# Personal Expense Tracker

CATEGORIES = ("Food", "Transport", "Bills", "Shopping", "Others") #tuple
expenses = []


def load_expenses(filename="expenses.txt"):
    global expenses
    expenses = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split("|")
                if len(parts) != 4:
                    continue

                amount_str, category, description, date = parts

                try:
                    amount = float(amount_str)
                except ValueError:
                    continue

                if category not in CATEGORIES:
                    category = "Others"

                expenses.append({
                    "amount": amount,
                    "category": category,
                    "description": description,
                    "date": date
                })
    except FileNotFoundError:
        pass


def save_expenses(filename="expenses.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for e in expenses:
            f.write(f"{e['amount']}|{e['category']}|{e['description']}|{e['date']}\n")
    print("Expenses saved.")


def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Enter a valid number.")


def get_category():
    while True:
        print("\nChoose category:")
        for i, cat in enumerate(CATEGORIES, start=1):
            print(f"{i}. {cat}")

        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print("Your input number is wrong, please choose a valid number between 1 to 5.")
        except ValueError:
            print("Enter a number.")


def add_expense():
    amount = get_amount()
    category = get_category()
    description = input("Description: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()

    if description == "":
        description = "No description"
    if date == "":
        date = "No date"

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })
    print("Your Expense added.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found. Please add your expense")
        return

    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ${e['amount']:.2f} | {e['category']} | {e['description']} | {e['date']}")

    used_categories = {e["category"] for e in expenses}
    used_dates = {e["date"] for e in expenses}

    print("Unique categories:", ", ".join(sorted(used_categories)))
    print("Unique dates:", ", ".join(sorted(used_dates)))


def view_summary():
    if len(expenses) == 0:
        print("No expenses to summarize.Please add your expense2")
        return

    total = sum(e["amount"] for e in expenses)
    average = total / len(expenses)

    print(f"Total spent: ${total:.2f}")
    print(f"Average spending: ${average:.2f}")

    print("Spent per category:")
    for cat in CATEGORIES:
        cat_total = sum(e["amount"] for e in expenses if e["category"] == cat)
        print(f"- {cat}: ${cat_total:.2f}")


def menu(user_name):
    while True:
        print(f"\nHello {user_name}, choose an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Save and Exit")

        choice = input("Option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_expenses()
            break
        else:
            print("Please choose 1 to 4.")


# -------- PROGRAM START --------
print("Welcome to Personal Expense Tracker")

user_name = input("Please enter your name: ").strip()
if user_name == "":
    user_name = "User"

load_expenses()
menu(user_name)
