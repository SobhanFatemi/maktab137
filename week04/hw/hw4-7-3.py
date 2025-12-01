class InvalidOperator(Exception):
    """Invalid operator"""

def calculator(*args, **kwargs):
        if kwargs["operator"] == '+':
            return args[0] + args[1]

        elif kwargs["operator"] == '-':
            return args[0] - args[1]

        elif kwargs["operator"] == '*':
            return args[0] * args[1]

        elif kwargs["operator"] == '/':
            return args[0] / args[1]

while True:
    try:
        first_num = int(input("Enter your first number: "))
        second_num = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid input!")
        continue
    try:
        operator_input = input("Enter your operator: ")

        if operator_input != "+" and operator_input != "-" and operator_input != "*" and operator_input != "/":
            raise InvalidOperator
    except InvalidOperator:
        print("Invalid input!")
        continue
    
    if operator_input == "/" and second_num == 0:
        print("Can not divide by 0!")
        continue

    result = calculator(first_num, second_num, operator=operator_input)

    print(f"{first_num} {operator_input} {second_num} = {result}")

    user_choice = ""
    while user_choice != "more" and user_choice != "quit":
        user_choice = input("To do more calculation type 'more' and to quit type 'quit': ")
    
    if user_choice == "more":
        continue
    else:
        break