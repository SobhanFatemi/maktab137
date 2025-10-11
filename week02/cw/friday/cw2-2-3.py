def check_num(num):
    try:
        if num < 0:
            raise ValueError
    except ValueError:
        print("Please enter a non negative number!")

check_num(-1)
        