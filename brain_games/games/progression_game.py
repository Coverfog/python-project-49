from random import randint


def progression_game():
    start_sentence = "What number is missing in the progression?"

    start = randint(1, 20)
    step = randint(2, 10)
    progression = create_progression(start, step)

    answer_index = randint(0, 9)
    correct_answer = progression[answer_index]

    progression[answer_index] = '..'
    progression_string = ' '.join(progression)

    question = f'Question: {progression_string}'
    
    return start_sentence, question, correct_answer


def create_progression(start, step):
    index = 0
    progression = []

    while len(progression) < 10:
        current_element = start + index * step
        progression.append(str(current_element))
        index += 1

    return progression
