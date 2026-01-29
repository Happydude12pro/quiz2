import csv
import types


def load_questions(filename):
    questions = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        next(csv_reader)

        for line in csv_reader:
            line['answers'] = line['answers'].split(';')
            questions.append(line)
    return questions


questions = load_questions('quiz_questions.csv')

def print_question(question):
    print("Category:    " + question['category'])
    print("Question:    " + question['question'])
    print("Here are your Options: :)")
    print(" / ".join(f"{i}. {opt}" for i, opt in enumerate(question['answers'], start=1)))
    Option_chosen=input()

    while not Option_chosen.isdigit():
        Option_chosen = input("Please try again!")

    Option_chosen = int(Option_chosen)


for x in questions:
    print_question(x)


