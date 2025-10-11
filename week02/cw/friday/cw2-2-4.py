file_name = input("Please enter the name of the file you want to create: ")
counter = 1
with open(f"{file_name}.txt", 'a') as file:
    while True:
        try:
            user_input = input(f"Line # {counter}: \n")
            if counter > 1:
                file.write(f"\n{user_input}")
            else:
                file.write(user_input)
            counter += 1
        except KeyboardInterrupt:
            break

with open(f"{file_name}.txt", 'r') as file:
    for line in file:
        print(line.strip())