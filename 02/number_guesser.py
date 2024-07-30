import random


def print_welcome_message():
    print("Welcome to the Number Guessing Game!")


def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    # Set the range for the guessing game
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}")

    while True:
        user_guess = get_user_input("Your guess: ")
        attempts += 1

        if user_guess < lower_bound or user_guess > upper_bound:
            print(f"Please guess a number between {lower_bound} and {upper_bound}.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
            )
            break


def main():
    print_welcome_message()

    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
