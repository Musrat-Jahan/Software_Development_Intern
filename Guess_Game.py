import random

def ask_yes_no(message):
    while True:
        answer = input(message).strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Invalid input. Please enter yes or no.")

def choose_option():
    while True:
        choice = input("Choose your option (Easy / Hard): ").strip().lower()

        if choice in ("easy", "e"):
            return 10, 5, "Easy"
        elif choice in ("hard", "h"):
            return 50, 3, "Hard"
        else:
            print('Invalid input. Please type "Easy" or "Hard".')

def play_game():
    max_number, attempts, level = choose_option()
    secret_number = random.randint(1, max_number)

    print(f"\nThe secret number is between 1 and {max_number}.")
    print(f"For {level} option, you have {attempts} attempts.\n")

    remaining_attempts = attempts

    while remaining_attempts > 0:
        guess_input = input("Enter your guessing number: ").strip()

        # Check if numeric (avoids crash)
        if not guess_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess_input)

        # Check range
        if guess < 1 or guess > max_number:
            print(f"Invalid number. Enter a number between 1 and {max_number}.")
            continue

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            used_attempts = attempts - remaining_attempts + 1
            print(f"🎉 Your guessing number is Correct! You guessed it in {used_attempts} attempts from {attempts}.")
            print(f"The secret number was {secret_number}.")
            return

        remaining_attempts -= 1
        print(f"Attempts left: {remaining_attempts}\n")

    print(f"Oops! Game Over! The secret number was {secret_number}.")
    print("Good luck next time!")

def main():
    print("***************Welcome to Smart Number Guessing Game.***********")
    print("The game picks a random secret number and the player guesses it.")

    if not ask_yes_no("\nDo you want to start the game? (yes/no): "):
        print("Goodbye")
        return

    while True:
        play_game()
        if not ask_yes_no("\nDo you want to play another round? (yes/no): "):
            print("Thanks for playing!")
            break

main()
