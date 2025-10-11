counter = 0
with open('lorenm.txt', 'r') as file:
    for line in file:
        counter += len(line.split())

print(counter)