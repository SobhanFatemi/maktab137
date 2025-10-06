def convert_time(seconds):
    hour = seconds // 3600
    minute = (seconds // 60) - (hour * 60)
    second = seconds - (minute * 60) - (hour * 3600)
    print(f"{hour}:{minute}:{second}")

convert_time(3670)