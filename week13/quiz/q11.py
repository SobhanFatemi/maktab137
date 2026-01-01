class Calculator:

    def __init__(self):
        self.history = []
    
    def add(self, first_num, second_num):
        result = first_num + second_num
        self.history.append(f"{first_num} + {second_num} = {result}")
        return result
    
    def sub(self, first_num, second_num):
        result = first_num - second_num
        self.history.append(f"{first_num} - {second_num} = {result}")
        return result
    
    def multiply(self, first_num, second_num):
        result = first_num * second_num
        self.history.append(f"{first_num} * {second_num} = {result}")
        return result
    
    def divide(self, first_num, second_num):
        if second_num == 0:
            self.history.append(f"{first_num} / {second_num} = ERROR")
            return "ZeroDivision Error!"
        result = first_num / second_num
        self.history.append(f"{first_num} / {second_num} = {result}")
        return result
    
    def get_history(self):
        return self.history


calc = Calculator()

print(calc.add(4, 5))
print(calc.multiply(3, 7))
print(calc.divide(10, 0))

print("History:")
for h in calc.get_history():
    print(h)