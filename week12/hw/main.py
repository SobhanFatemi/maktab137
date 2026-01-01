from reminder_model import ReminderManager
from logger import logger

def main():
    rm = ReminderManager()
<<<<<<< HEAD
    group = []
    while True:
        menu_choice = input("Please enter your desired choice:\n" \
                            "1- Create a new reminder\n" \
                            "2- Remove a reminder\n" \
                            "3- Show all reminders\n" \
                            "4- Find reminder using ID\n" \
                            "5- Execute reminder using ID\n" \
                            "6- Execute all reminders\n" \
                            "7- Group reminders\n" \
                            "8- Exit\n" \
=======
    while True:
        menu_choice = input("Please enter your desired choice:\n" \
                            "1- Create new remider\n" \
                            "2- Remove a reminder\n" \
                            "3- Show all reminders\n" \
                            "4- Find reminder using ID\n" \
                            "5- Execute all reminders\n" \
                            "6- Group reminders\n" \
                            "7- Exit\n" \
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
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
<<<<<<< HEAD
                group = []
=======
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
                continue
            
            elif reminder_type == '2':
                rm.add_reminder("meeting")
<<<<<<< HEAD
                group = []
=======
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
                continue

            elif reminder_type == '3':
                rm.add_reminder("daily")
<<<<<<< HEAD
                group = []
=======
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
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
<<<<<<< HEAD
            if not group:
                rm.show()
                continue
            else:
                execution_choice = input("Please enter your desired choice:\n" \
                            "1- Show group\n" \
                            "2- Show all\n" \
                            "3- Exit\n" \
                            "Your choice: ")
                if execution_choice == '1':
                    rm.show(group)
                    continue
                elif execution_choice == '2':
                    rm.show()
                    continue
                elif execution_choice == '3':
                    continue
                else:
                    logger.error("Invalid input!")
                    continue
=======
            rm.show_all()
            continue
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b

        elif menu_choice == '4':
            id = input("Please enter the ID of the reminder you want: ")
            if rm.id_exists(id):
                rm.find_by_id(id)
                continue
            else:
                logger.warning(f"'{id}' was not found!")
                continue

        elif menu_choice == '5':
<<<<<<< HEAD
            id = input("Please enter the ID of the reminder you want: ")

            reminder = rm.id_exists(id)

            if not reminder:
                logger.warning(f"'{id}' was not found!")
            else:
                rm.execute([reminder])
                group = []
            
        elif menu_choice == '6':
            if not group:
                rm.execute()
                continue
            else:
                execution_choice = input("Please enter your desired choice:\n" \
                            "1- Execute group\n" \
                            "2- Execute all\n" \
                            "3- Exit\n" \
                            "Your choice: ")
                if execution_choice == '1':
                    rm.execute(group)
                    group = []
                    continue
                elif execution_choice == '2':
                    rm.execute()
                    group = []
                    continue
                elif execution_choice == '3':
                    continue
                else:
                    logger.error("Invalid input!")
                    continue

        elif menu_choice == '7':
            if group:
                type_choice_option = input("Please enter the type you want shown:\n" \
                                "1- Simple\n" \
                                "2- Meeting\n" \
                                "3- Daily routine\n" \
                                "4- Empty group"
                                "5- Exit\n" \
                                "Your choice: ")
            
                if type_choice_option == '1':
                    type_choice = "simple"

                elif type_choice_option == '2':
                    type_choice = "meeting"

                elif type_choice_option == '3':
                    type_choice = "daily"

                elif type_choice_option == '4':
                    group = []
                    continue

                elif type_choice_option == '5':
                    continue
                
                else:
                    logger.error("Invalid input!")
                    continue
                
            else:
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
            
=======
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

>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
            group = rm.reminder_group(type_choice)

            if not group:
                logger.warning(f"No reminders of type '{type_choice}' found.")
            else:
<<<<<<< HEAD
                rm.show(group)

        elif menu_choice == '8':
=======
                rm.show_all(group)

        elif menu_choice == '7':
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
            logger.info("Exiting program...")
            break            
        
        else:
<<<<<<< HEAD
            logger.error("Invalid input!")
=======
            logger.error("Invalid input")
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
            continue
        
if __name__ =="__main__":
    main()