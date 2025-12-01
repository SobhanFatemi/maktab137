first_input = "aBcD"
second_input = "ABcd"

# first_input = input("Enter your first sentence: ")
# second_input = input("Enter your second sentence: ")

counter = 0
for first_letter, second_letter in zip(first_input, second_input):
    if first_letter == second_letter:
        counter += 1

print(counter)