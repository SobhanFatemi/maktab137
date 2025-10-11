def loop(n):
    print(f'loop in {n}')
    if n > 0:
        loop(n-1)

loop(2)