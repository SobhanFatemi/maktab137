num_sum = 0

while True:
    try:
        num = input()
    except KeyboardInterrupt:
        print('sum = ', num_sum)
        break

    try:
        num = int(num)
        num_sum += num
    except ValueError:
        try:
            num = float(num)
            num_sum += num
        except ValueError:
            print('Enter an integer or float!')