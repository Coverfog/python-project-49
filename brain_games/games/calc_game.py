from random import choice, randint


def calc_game():
    start_sentence = "What is the result of the expression?"
    operators = ['+', '-', '*']
    operator = choice(operators)

    match operator:
        case '+':
            num1 = randint(1, 20)
            num2 = randint(1, 20)
            result = num1 + num2
        case '-':
            num1 = randint(10, 20)
            num2 = randint(1, 10)
            result = num1 - num2
        case '*':
            num1 = randint(1, 20)
            num2 = randint(2, 5)
            result = num1 * num2

    question = f"Question: {str(num1)} {operator} {str(num2)}"
    correct_answer = str(result)

    return start_sentence, question, correct_answer
