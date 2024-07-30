def welcome_message():
    print("Welcom to my computer quiz!")


def get_user_input(prompt):
    return input(prompt).strip().lower()


def ask_question(question, answer):
    user_answer = get_user_input(question)
    return answer == user_answer.lower()


def quiz():
    questions_and_answers = {
        "What does CPU stand for? ": "central processing unit",
        "What does RAM stand for? ": "random access memory",
        "What is the brain of the computer? ": "cpu",
        "What does GPU stand for? ": "graphics processing unit",
    }

    score = 0
    for questions, answers in questions_and_answers.items():
        if ask_question(questions, answers):
            score += 1
            print("Correct Answer!")
        else:
            print("Wrong Answer!")

    print(f"Your final score is: {score}/{len(questions_and_answers)}")


def main():
    welcome_message()

    playing = get_user_input("Do you wants to play game? (yes/no) ")

    if playing != "yes":
        print("Exiting the quiz. Have a great day! :) ")
        quit()
    quiz()


if __name__ == "__main__":
    main()
