from cw11_1_1_logger import logger

class User:
    def __init__(self, username, email, is_logged_in = False):
        self.username = username
        self.email = email
        self.is_logged_in = is_logged_in

    def login(self):
        if not self.is_logged_in:
            logger.info(f"Successful log in as '{self.username}'")
            print(f"You have logged in as '{self.username}'!")
            self.is_logged_in = True
        else:
            logger.warning(f"Unsuccessful log in attempt as '{self.username}'!")
            print(f"'{self.username}' is already logged in!")

    def logout(self):
        if self.is_logged_in:
            logger.info(f"Successful log out as '{self.username}'")
            print(f"You have logged out from '{self.username}'!")
            self.is_logged_in = False
        else:
            logger.warning(f"Unsuccessful log out attempt as '{self.username}'!")
            print(f"'{self.username}' is not logged in!")


def main(user):
    while True:
        menu_choice = input("Please enter you desired choice:\n" \
                                "1- Log in\n" \
                                "2- Log out\n" \
                                "3- Show status\n" \
                                "4- Exit program\n" \
                                "Your choice: ")
        
        if menu_choice == "1":
            user.login()
            continue

        elif menu_choice == "2":
            user.logout()
            continue

        elif menu_choice == "3":
            if user.is_logged_in:
                print(f"{user.username}  is logged in!")
                continue
            
            else:
                print(f"{user.username} user is logged in!")
                continue

        elif menu_choice == "4":
            print("Exiting program...")
            break
        
        else:
            logger.warning(f"Wrong menu input!")
            print("Invalid input!")
            continue

if __name__ == "__main__":
    user = User("Sobhan", "sobhanfatemi55@gmail.com")
    main(user)