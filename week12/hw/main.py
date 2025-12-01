from reminder_model import ReminderManager
from logger import logger

def main():
    rm = ReminderManager()
    while True:
        menu_choice = input("Please enter your desired choice:\n" \
                            "1- Create new remider\n" \
                            "2- Remove a reminder\n" \
                            "3- Show all reminders\n" \
                            "4- Find reminder using ID\n" \
                            "5- Execute all reminders\n" \
                            "6- Group reminders\n" \
                            "7- Exit\n" \
                            "Your choice: ")
        
        if menu_choice == '1':
            reminder_type = input("Please enter your desired reminder type:\n" \
                            "1- Simple reminder\n" \
                            "2- Meeting reminder\n" \
                            "3- Daily reminder\n" \
                            "4- Exit\n" \
                            "Your choice: ")
            if reminder_type == '1':
                rm.add_reminder("simple")
                continue
            
            elif reminder_type == '2':
                rm.add_reminder("meeting")
                continue

            elif reminder_type == '3':
                rm.add_reminder("daily")
                continue

            elif reminder_type == '4':
                continue

            else:
                logger.error("Invalid input!")
                continue
        
        elif menu_choice == '2':
            id = input("Please enter the ID of the reminder you want to remove: ")
            if rm.id_exists(id):
                rm.remove_reminder(id)
                continue
            else:
                logger.warning(f"'{id}' was not found!")
                continue
        
        elif menu_choice == '3':
            rm.show_all()
            continue

        elif menu_choice == '4':
            id = input("Please enter the ID of the reminder you want: ")
            if rm.id_exists(id):
                rm.find_by_id(id)
                continue
            else:
                logger.warning(f"'{id}' was not found!")
                continue

        elif menu_choice == '5':
            rm.execute_all()
            continue

        elif menu_choice == '6':
            type_choice_option = input("Please enter the type you want shown:\n" \
                                "1- Simple\n" \
                                "2- Meeting\n" \
                                "3- Daily routine\n" \
                                "4- Exit\n" \
                                "Your choice: ")
            
            if type_choice_option == '1':
                type_choice = "simple"

            elif type_choice_option == '2':
                type_choice = "meeting"

            elif type_choice_option == '3':
                type_choice = "daily"

            elif type_choice_option == '4':
                continue
            
            else:
                logger.error("Invalid input!")
                continue

            group = rm.reminder_group(type_choice)

            if not group:
                logger.warning(f"No reminders of type '{type_choice}' found.")
            else:
                rm.show_all(group)

        elif menu_choice == '7':
            logger.info("Exiting program...")
            break            
        
        else:
            logger.error("Invalid input")
            continue
        
if __name__ =="__main__":
    main()