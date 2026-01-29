import csv
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
    print(question['category'], question['question'], question['answers'])


for x in questions:
    print_question(x)