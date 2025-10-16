numbers = [1, 2, 3, 4, 5, 6, 7, 8]
new_numbers = list(map(lambda n: n**3, filter(lambda n: n % 2 != 0, numbers)))
print(new_numbers)