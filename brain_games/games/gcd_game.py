from random import randint


def gcd_game():
    start_sentence = "Find the greatest common divisor of given numbers."

    multiplier = randint(2, 5)
    num1 = randint(1, 20) * multiplier
    num2 = randint(1, 20) * multiplier

    question = f"Question: {num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))

    return start_sentence, question, correct_answer


def find_gcd(num1, num2):

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1
