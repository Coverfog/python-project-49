import prompt


def start_game(game, user):
    acc = 0

    while acc < 3:
        start_sentence, question, correct_answer = game()

        if acc == 0:
            print(start_sentence)

        print(question)
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print("Correct!")
            acc += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user}!")
            return None

    print(f"Congratulations, {user}!")
