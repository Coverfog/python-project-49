import random

import prompt


def calc_game(user):
    acc = 0
    actions = ['+', '-', '*']

    print("What is the result of the expression?")

    while acc < 3:
        action = random.choice(actions)

        if action == '+':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            result = num1 + num2
        elif action == '-':
            num1 = random.randint(10, 20)
            num2 = random.randint(1, 10)
            result = num1 - num2
        elif action == '*':
            num1 = random.randint(1, 20)
            num2 = random.randint(2, 5)
            result = num1 * num2

        print(f'Question: {str(num1)} {str(action)} {str(num2)}')
        answer = prompt.string('Your answer: ')

        if answer == str(result):
            print("Correct!")
            acc += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{str(result)}".')
            print(f"Let's try again, {user}!")
            return None
