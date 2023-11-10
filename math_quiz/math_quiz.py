import random


def get_random_int(min: int, max: int) -> int:
    """Returns a random value between min & max

    Args:
        min (int): Minimum value
        max (int): Maximum value

    Returns:
        int: Random integer
    """
    return random.randint(min, max)


def get_math_operator() -> str:
    """Returns a random math operator from [+,-,*]

    Returns:
        str: Math operator
    """
    return random.choice(["+", "-", "*"])


def generate_question(num_1: int, num_2: int, operator: str) -> tuple[str, int]:
    """Returns a math question

    Args:
        num_1 (int): First number
        num_2 (int): Second number
        operator (str): Math operator

    Returns:
        tuple[str, int]: Returns a tuple of problem (str) and answer (int)
    """
    problem = f"{num_1} {operator} {num_2}"
    if operator == "+":
        answer = num_1 + num_2
    elif operator == "-":
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems, and you need to provide the correct answers."
    )

    for _ in range(total_questions):
        num_1 = get_random_int(1, 10)
        num_2 = get_random_int(1, 5)
        operator = get_math_operator()

        problem, answer = generate_question(num_1, num_2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = int(input("Your answer: "))

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
