from datetime import datetime

minute = datetime.now().minute
hour = datetime.now().hour

def restrict_hours(start, end):
    def decorator(func):
        def wrapper():
            if start <= hour < end:
                result = func()
                return result
            else:
                if minute == 0:
                    hours_remaining = 24 - hour
                    minutes_remaining = 0
                else:
                    hours_remaining = 23 - hour + start
                    minutes_remaining = 60 - minute
                print(f"Come back in {hours_remaining} hours and {minutes_remaining} minutes.")
        return wrapper
    return decorator


@restrict_hours(start=9, end=17)
def do_work():
    print("Working...")

do_work()