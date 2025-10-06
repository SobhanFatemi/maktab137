def type_dependant(user_input):
    if type(user_input) == int:
        return user_input ** 2
    elif type(user_input) == str:  
        return len(user_input)
    elif type(user_input) == list:
        return sum(user_input)
    
print(type_dependant(3))
print(type_dependant("Sobhan"))
print(type_dependant([5, 53, 32]))