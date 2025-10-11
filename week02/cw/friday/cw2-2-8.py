import csv

students = []
with open("cw2-2-7.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        students.append(line)

for student in students:
    if float(student[2]) > 15:
        print(student[0])