from math_op import add, sub

import math

def greet(name, message):
    return f"{name}, {message}"

print(greet("Sobhan","Hello"))

# print(greet("Sobhan"))

print(greet("Hello","Sobhan"))

print(greet(message = "Hello", name = "Sobhan"))


def pow(first_num, second_num = 2):
    return first_num ** second_num

print(pow(10))

print(pow(10, 3))


def sum_tuple_sequence(numbers):
    return sum(numbers)

tup = (1, 2, 3, 4, 5)

print(tup[2:4])

print(sum_tuple_sequence(tup))


def sum_using_args(*args):
    return sum(args)

print(sum_using_args(1, 2, 3, 4, 5))

print("dictionery".center(50, "-"))
person: dict = {
    "name": "Sobhan",
    "age": 23,
    "city": "Tehran"
}

for items in person:
    print(items, person[items])


print("dictionery whith item".center(50, "-"))
for (key, value) in person.items():
    print(key, value)

person.update({"country": "Iran"})

print("dictionery whith item updated".center(50, "-"))
for (key, value) in person.items():
    print(key, value)

print(person.get("country", "US"))
print(person.get("sex", "M"))

def check_age(age):
    if age < 18:
        return
    
    days = age * 365
    return days

print(check_age(18))
print(check_age(3))

# return is a tuple
def change_values(num_1, num_2):
    return num_2, num_1

# unpacking items
item_1, item_2 = change_values(1, 2)

print(item_1, item_2)


print("item 1: ", item_1)
print("item 2: ", item_2)
item_1, item_2 = change_values(item_1, item_2)
print("item 1: ", item_1)
print("item 2: ", item_2)

num_1 = 25
num_2 = 98

print(add(num_1, num_2))

sqrt = math.sqrt(num_1)

print(f"{num_1} sqrt is: {sqrt}")


result = 0

first_number = int(input("First number: "))
second_number = int(input("second number: "))

try:
    result = first_number / second_number
    is_success = True
except ZeroDivisionError:
  print("Please don't use zero for second number.")
  is_success = False
except TypeError as error:
    print(f"The error is: {error}")
finally:
    print(f"Operation finished {'successfully' if is_success else 'unsuccessfully'}")

print(f"{first_number} / {second_number} = {result}")

def operate():
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        result: int = first_number / second_number
        return result
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError as error:
        print(f"TypeError: {error}") #?
    else: # execution ?
        print("Operation successful")
    finally:
        print("End") # execution ?

result = operate()
print(result)