import json
from datetime import datetime
from logger import logger

def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_json_file_append(filepath, data):
    reminders = read_json_file(filepath)
    reminders.append(data)
    
    with open(filepath, 'w') as file:
        json.dump(reminders, file, indent=4)

def save_json_file_overwrite(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def get_timer_input():
    while True:
        timer_input = input("Enter the time [HH:MM]: ")
        try:
            timer_dt = datetime.strptime(timer_input, "%H:%M")
            formatted_timer = timer_dt.strftime("%H:%M")
            return formatted_timer
        except ValueError:
            logger.error("Invalid format! Please use HH:MM")