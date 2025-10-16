class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        print(f"{self.name}'s base salary is: {self.base_salary}")

    def info(self):
        print(f"Employee: {self.name}, Base salary: {self.base_salary}")


class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        print(f"{self.name}'s total salary is: {self.bonus + self.base_salary}")


class PartTimeEmployee(Employee):
    def __init__(self, name, base_salary, hourly_rate, hours_worked):
        super().__init__(name, base_salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        print(f"{self.name}'s total salary is: {self.hours_worked * self.hourly_rate}")


employee1= Employee("Sobhan", 18)
employee1.calculate_salary()
employee1.info()

employee2 =  FullTimeEmployee("Ali", 18, 4)
employee2.info()
employee2.calculate_salary()
employee3 = PartTimeEmployee("Zahra", 18, 0.5 , 40)
employee3.info()
employee3.calculate_salary()
