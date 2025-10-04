
first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))
operator = input("Please enter your operator (+ or - or / or *): ")

result: float = 0

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    print("Please enter a correct operator!")

print(f"{first_number} {operator} {second_number} = {result}")