def convert(usr_inpt):
    try:
        return int(usr_inpt)
    except ValueError:
        return "Please enter an integer!"

print(convert("2"))
print(convert("S"))