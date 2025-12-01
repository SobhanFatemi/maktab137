from config import REMINDER_FILE
from utils import read_json_file

def load_last_id():
    reminders = read_json_file(REMINDER_FILE)
    if reminders:
        return max(int(key) for reminder in reminders for key in reminder)
    else:
        return 100


def gen_id_generator():
    last_id = load_last_id()
    while True:
        last_id += 1
        yield last_id


id_gen = gen_id_generator()

def gen_id():
    return next(id_gen)