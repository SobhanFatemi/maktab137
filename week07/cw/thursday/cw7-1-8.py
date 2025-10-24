class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        if not isinstance(other, Employee):
            raise ValueError("Value must be a Employee!")
        return self.name == other.name
    
    def __add__(self, other):
        if not isinstance(other, Employee):
            raise ValueError("Value must be a Employee!")
        if self == other:
            return Employee(self.name, self.salary + other.salary)
        return Employee(f"{self.name} & {other.name}", self.salary + other.salary)
    
    def __str__(self):
        return f"'{self.name}': '${self.salary}'"
    
    def __del__(self):
        print(f"'{self.name}' was deleted from memory!")


e1 = Employee("Alice", 5000)
e2 = Employee("Alice", 4500)
e3 = Employee("Bob", 6000)

print(e1)  
print(e3)  

print(e1 == e2)  
print(e1 == e3)  

e4 = e1 + e2
print(e4)  

e5 = e1 + e3
print(e5)  