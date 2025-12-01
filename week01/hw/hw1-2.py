a = int(input("Please enter your number: "))

i: int = 1
x: int = 0

while i < a:
    if a % i == 0:
        x += i
    i += 1

if x == a:
    print("YES")
else:
    print("NO")