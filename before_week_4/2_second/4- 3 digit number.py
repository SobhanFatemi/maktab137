user_input = int(input("Please enter your number: "))

first_digit = user_input // 100
second_digit = (user_input // 10) % 10
third_digit = user_input % 10

print("Result: ", first_digit + second_digit + third_digit)