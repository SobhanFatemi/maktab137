user_input: list = list(input("Please enter your name: "))

i: int = 0

while i < len(user_input):
    if user_input[i] == " ":
        del user_input[i]

    if user_input[i] == "a" or  user_input[i] == "e" or  user_input[i] == "i" or  user_input[i] == "o" or  user_input[i] == "u" or  user_input[i] == "A" or  user_input[i] == "E" or  user_input[i] == "I" or  user_input[i] == "O" or  user_input[i] == "U":
        user_input[i] = "."
    i += 1

user_input.reverse()

# found this line in stackoverflow
user_input_str: str = ''.join(user_input)

print(user_input_str)