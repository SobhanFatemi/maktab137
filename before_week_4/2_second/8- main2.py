age: int = int(input("Please entet yout age: "))

if 0 < age < 18:
    print("You can not enter!")
elif 100 > age >= 18:
    print("You may enter!")
else:
    print("Invalid input!")