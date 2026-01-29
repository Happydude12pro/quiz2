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


load_questions('quiz_questions.csv')


