from random import randint


def even_game():
    start_sentence = (
    'Answer "yes" if the number is even, otherwise answer "no".'
    )

    num = randint(1, 20)
    question = f'Question: {str(num)}'
    correct_answer = is_even(num)

    return start_sentence, question, correct_answer


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
