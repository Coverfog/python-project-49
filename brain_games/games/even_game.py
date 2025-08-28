from random import randint

import prompt


def even_game(user):
    acc = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while acc < 3:
        num = randint(1, 20)

        print(f'Question: {str(num)}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(num)

        if answer == correct_answer:
            print("Correct!")
            acc += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user}!")
            return None

    print(f"Congratulations, {user}!")
    return None


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
