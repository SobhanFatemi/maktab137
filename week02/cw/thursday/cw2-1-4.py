def prime_finder(num):
    while True:
        is_prime = True
        num += 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime == True:
            return num
        else:
            continue
    
print(prime_finder(25))
