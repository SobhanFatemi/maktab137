import csv

students = [("Sobhan", 23, 11.2), ("Fateme", 20, 19.5), ("Arman", 15, 19)]

with open("cw2-2-7.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    for student in students:
        writer.writerow(student)