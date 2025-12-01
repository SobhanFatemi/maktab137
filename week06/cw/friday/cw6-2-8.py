class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def set_name(self, new_name):
        self.__name = new_name

    def set_salary(self, new_salary):
        self.__salary = new_salary


employee = Employee("John Doe", 5000.0)
print(employee.get_name())

print(employee.get_salary())

employee.set_name("Jane Smith")
employee.set_salary(6000.0)
print(employee.get_name())

print(employee.get_salary())
try:
    print(employee.__name)
except AttributeError:
    print("Can't access private attribute!")
