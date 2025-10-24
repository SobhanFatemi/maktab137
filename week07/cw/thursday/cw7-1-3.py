class Student:
    def __init__(self, name, grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.grades = grades

    def __len__(self):
        return len(self.grades)

    def __add__(self, other):
        if not isinstance(other, Student):
            raise ValueError("Value must be a Student!")
        return Student(f"{self.name} & {other.name}", self.grades + other.grades)
    
    def __str__(self):
        try:
            avg = sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            avg = 0
        return f"'{self.name}': '{avg:.2f}'"
    
    def __del__(self):
        print(f"'{self.name}' was deleted from memory!")

s1 = Student("Alice", [85, 90, 78])
s2 = Student("Bob", [92, 88])
s3 = Student("Charlie") 

print(s1)  
print(s2)  
print(s3)  


combined = s1 + s2
print(combined)  


print(len(s1))
print(len(s3))  

        