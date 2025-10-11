with open('cw2-2-5.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 20:
            break
        print(line.strip())