temp: int = int(input("Please enter your tempreture: "))

if temp < 10:
    print("It's cold")
elif 10 <= temp <= 25:
    print("It's moderate")
elif temp > 25:
    print("It's hot")