name: str = input("Please enter your name: ")
score: float = float(input("Please enter your score: "))

if score > 90:
    print(f"{name}: Great")
elif 70 <= score <= 90:
    print(f"{name}: Good")
elif score < 70:
    print(f"{name}: Needs more practice")