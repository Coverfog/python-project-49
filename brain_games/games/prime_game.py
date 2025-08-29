from random import randint


def prime_game():
    start_sentence = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
    )

    num = randint(0, 100)

    question = f"Question: {num}"
    correct_answer = is_prime(num)

    return start_sentence, question, correct_answer


def is_prime(num):

    if num <= 1:
        return 'no'

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'

    return 'yes'
