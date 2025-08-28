from random import choice, randint


def calc_game():
    start_sentence = "What is the result of the expression?"
    actions = ['+', '-', '*']
    action = choice(actions)

    if action == '+':
        num1 = randint(1, 20)
        num2 = randint(1, 20)
        result = num1 + num2
    elif action == '-':
        num1 = randint(10, 20)
        num2 = randint(1, 10)
        result = num1 - num2
    elif action == '*':
        num1 = randint(1, 20)
        num2 = randint(2, 5)
        result = num1 * num2

    question = f"Question: {str(num1)} {action} {str(num2)}"
    correct_answer = str(result)

    return start_sentence, question, correct_answer
