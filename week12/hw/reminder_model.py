from dataclasses import dataclass, field
from abc import ABC
from utils import save_json_file_append, save_json_file_overwrite, read_json_file, get_timer_input
from id_generator import gen_id
from config import REMINDER_FILE
from logger import logger

@dataclass
class Reminder(ABC):
    reminder: str
    timer_set: str

@dataclass
class SimpleReminder(Reminder):
    save: bool
    id: int = field(default_factory = gen_id)

    def __post_init__(self):
        if self.save:
            data = {
                self.id: {
                    "reminder": self.reminder,
                    "timer": self.timer_set,
                    "type": "simple"
                }
            }
            save_json_file_append(REMINDER_FILE, data)
    
    def remind(self):
        logger.info(f"It's '{self.timer_set}', time to '{self.reminder}'!")
        rm = ReminderManager()
        rm.remove_reminder(str(self.id))
    
@dataclass
class MeetingReminder(Reminder):
    participants: list
    save: bool
    id: int = field(default_factory = gen_id)

    def __post_init__(self):
        if self.save:
            data = {
                self.id: {
                    "reminder": self.reminder,
                    "participants": self.participants,
                    "timer": self.timer_set,
                    "type": "meeting"
                }
            }
            save_json_file_append(REMINDER_FILE, data)
    
    def remind(self):
        logger.info(f"It's '{self.timer_set}', time to '{self.reminder}'!\tParticipants in that meeting: "
                    f"{' - '.join(self.participants)}")
        rm = ReminderManager()
        rm.remove_reminder(str(self.id))

@dataclass 
class DailyRoutineReminder(Reminder):
    remind_daily: bool
    save: bool
    id: int = field(default_factory = gen_id)

    def __post_init__(self):
        if self.save:
            if self.remind_daily:
                remind_daily_str = "Yes"
            else:
                remind_daily_str = "No"
            data = {
                self.id: {
                    "reminder": self.reminder,
                    "remind_daily": remind_daily_str,
                    "timer": self.timer_set,
                    "type": "daily"
                }
            }
            save_json_file_append(REMINDER_FILE, data)
    
    def remind(self):
        if self.remind_daily:
            logger.info(f"It's '{self.timer_set}', time to '{self.reminder}'! (Daily routine is on!)")
        else:
            logger.info(f"It's '{self.timer_set}', time to '{self.reminder}'! (Daily routine is off!)")
        rm = ReminderManager()
        rm.remove_reminder(str(self.id))


@dataclass
class ReminderManager():
    def add_reminder(self, type):
        reminder = input("Please enter your reminder: ")
        timer_set = get_timer_input()
        if type == "simple":
            logger.info("Created a 'simple' reminder")
            return SimpleReminder(reminder, timer_set, True)
        
        elif type == "meeting":
            participants_str = input("Please enter participants [Ali-Sara]: ")
            participants = participants_str.split('-')
            logger.info("Created a 'meeting' reminder") 
            return MeetingReminder(reminder, timer_set, participants, True)

        elif type == "daily":
            while True:
                daily_reminder = input("Do you want daily reminder to be activated? (y/n): ") 

                if daily_reminder == 'y':
                    logger.info("Created a 'daily routine' reminder") 
                    return DailyRoutineReminder(reminder, timer_set, True, True)
                
                elif daily_reminder == 'n':
                    logger.info("Created a 'daily routine' reminder") 
                    return DailyRoutineReminder(reminder, timer_set, False, True)
                
                else:
                    logger.error("Invalid input!")
                    continue
    
    def id_exists(self, id):
        reminders = read_json_file(REMINDER_FILE)

        for reminder in reminders:
            if list(reminder.keys())[0] == id:
<<<<<<< HEAD
                return reminder
        return None
=======
                return True
        return False
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b

    def find_by_id(self, id):
        reminders = read_json_file(REMINDER_FILE)

        for reminder in reminders:
            if list(reminder.keys())[0] == id:
                for key, value in reminder.items():
                    if value["type"] == "simple":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Type of timer: Simple\n")
                    
                    if value["type"] == "meeting":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Participants: {' - '.join(value["participants"])}\n" \
                            f"Type of timer: Meeting\n")
                    
                    if value["type"] == "daily":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Daily reminder: {"ON" if value["remind_daily"] == "Yes" else "OFF"}\n" \
                            f"Type of timer: Daily routine\n")

    def remove_reminder(self, id):
        reminders = read_json_file(REMINDER_FILE)

        if self.id_exists(id):
            reminders = [r for r in reminders if next(iter(r)) != id]
            logger.warning(f"Removed a reminder with the ID of '{id}'")
        
        else:
            logger.warning(f"'{id}'was not found!")

        save_json_file_overwrite(REMINDER_FILE, reminders)

<<<<<<< HEAD
    def show(self, reminders=None):
        if reminders is None:
            reminders = read_json_file(REMINDER_FILE)

        if not reminders:
            logger.warning("No reminders!")
            return
        
        else:
=======
    def show_all(self, reminders=read_json_file(REMINDER_FILE)):
        if reminders:
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
            for reminder in reminders:
                for key, value in reminder.items():
                    if value["type"] == "simple":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Type of timer: Simple\n")
                    
                    if value["type"] == "meeting":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Participants: {' - '.join(value["participants"])}\n" \
                            f"Type of timer: Meeting\n")
                    
                    if value["type"] == "daily":
                        print(f"{key}:\n" \
                            f"Timer set at: {value["timer"]}\n" \
                            f"Daily reminder: {"ON" if value["remind_daily"] == "Yes" else "OFF"}\n" \
                            f"Type of timer: Daily routine\n")
<<<<<<< HEAD
            
    def execute(self, reminders=None):
        if reminders is None:
            reminders = read_json_file(REMINDER_FILE)

        if not reminders:
            logger.warning("No reminders found!")
=======
        
        else:
            logger.warning("No reminders!")

    def execute_all(self):
        reminders = read_json_file(REMINDER_FILE)

        if not reminders:
            print("No reminders found!")
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
            return

        for reminder in reminders:
            for key, value in reminder.items():
                reminder_type = value["type"]

                if reminder_type == "simple":
                    reminder = SimpleReminder(value["reminder"], value["timer"], save=False)

                elif reminder_type == "meeting":
                    reminder = MeetingReminder(value["reminder"], value["timer"], value["participants"], save=False)

                elif reminder_type == "daily":
                    reminder = DailyRoutineReminder(value["reminder"], value["timer"], value["remind_daily"] == "Yes", save=False)

                reminder.id = int(key)
                
                reminder.remind()

    def reminder_group(self, reminder_type):
        reminders = read_json_file(REMINDER_FILE)
        group = []
        for reminder in reminders:
            for _ , value in reminder.items():
                if value["type"] == reminder_type:
                    group.append(reminder)
        return group