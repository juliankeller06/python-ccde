import random


class Question:
    def __init__(self, question_text, level, options, correct_index):
        self.question_text = question_text
        self.level = level
        self.options = options
        self.correct_index = correct_index


def read_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        for line in file:
            # Ignoriert Zeilen, die mit # beginnen
            if line.startswith("#"):
                continue

            parts = line.strip().split('\t')
            question_text = parts[1]
            level = int(parts[0])
            options = parts[2:6]
            correct_index = parts[2]
            random.shuffle(options)  # optionen mixxen
            questions.append(Question(question_text, level, options, correct_index))
    return questions


def get_random_question(level, questions):
    eligible_questions = [q for q in questions if q.level == level]
    return random.choice(eligible_questions)


def print_question(question):
    print(question.question_text)
    for i, option in enumerate(question.options):
        print(f"{i}. {option}")



def check_answer(question, user_answer):
    return question.options[int(user_answer)] == question.correct_index # String vergleich, NUR STRING INPUT EINGEBEN


if __name__ == '__main__':
    current_level = 0
    questions = read_questions("millionaire.txt")

    while current_level < 5:
        print(f'Your current level is {current_level}')
        question = get_random_question(current_level, questions)
        print_question(question)


        user_answer = input('Which answer? ')
        if check_answer(question, user_answer):
            print('Fine!')
            current_level += 1
        else:
            print('Wrong answer. Game over!')
            break