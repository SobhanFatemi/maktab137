def division(first_number, second_number):
    try:
        return first_number / second_number
    except ZeroDivisionError:
        return "Can't divide by 0!"

print(division(2, 2))
print(division(2, 0))
