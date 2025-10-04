total_minutes: str = input("Please enter your minutes: ")
total_minutes_int: int = int(total_minutes)
hour: int = total_minutes_int // 60
minutes: int = total_minutes_int % 60

print(f"You watched {hour} hours and {minutes} minutes")