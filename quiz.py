import random

from questions import get_questions
from scoring import calculate_score
from display import show_welcome


def main():
    show_welcome()
    questions = get_questions()
    score = calculate_score(questions)

    print(f"Poäng: {score}")


if __name__ == "__main__":
    main()
