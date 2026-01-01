class Student:
    def __init__(self, full_name, grades):
        self.full_name = full_name
        self.grades = grades

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        avg = sum(self.grades) / len(self.grades)
        print(avg)

student = Student('Ali Alavi', [18, 16, 20])

student.average()
student.add_grade(16)
student.average()