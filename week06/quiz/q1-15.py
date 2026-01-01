students = [
{"name": "Reza", "grade": 17},
{"name": "Sara", "grade": 19},
{"name": "Ali", "grade": 17},
{"name": "Mina", "grade": 20}
]
def sort(students):
    sorted_students = sorted(students, key=lambda x: (x['grade'], x['name']), reverse=True)
    return sorted_students

print(sort(students))