def fib_generator(n):
    counter = 0
    x = 0
    y = 1
    print(x)
    print(y)
    while counter < n - 2:
        z = x + y
        yield z
        x = y
        y = z
        counter += 1


user_input = int(input("Please enter a number: "))
for number in fib_generator(user_input):
    print(number)