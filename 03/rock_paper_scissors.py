import random


def print_welcome_message():
    print("Welcome to Rock-Paper-Scissors!")


def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"


def print_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("Sorry, the computer wins!")


def main():
    print_welcome_message()

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, winner)

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
