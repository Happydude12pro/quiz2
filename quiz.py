import csv
questions = []
with open('quiz_questions.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    next(csv_reader)
    Dic1 = {'quiz_questions.csv': []}


    for line in csv_reader:
        line['answers']=line['answers'].split(';')
        questions.append(line)
print(questions)




