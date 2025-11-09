from services.user_service import UserService


class AuthController:
    def __init__(self):
        self.service = UserService()

    def sign_in(self):
        while True:
            username = input("Please enter your username (q to quit): ").lower()
            if username == "q":
                return None

            if not (5 <= len(username) <= 15):
                print("Username must be 5–15 characters.")
                continue

            if self.service.username_exists(username):
                print("Username already exists!")
                continue

            password = input("Please enter your password: ")
            if not (6 <= len(password) <= 15):
                print("Password must be 6–15 characters!")
                continue

            first_name = input("Please enter your first name: ")
            last_name = input("Please enter your last name: ")

            try:
                ph = int(input("Please enter your phone number: "))
            except ValueError:
                print("Phone must be numeric!")
                continue

            try:
                year = int(input("Birth year (1925–2010): "))
                if not (1925 <= year <= 2010):
                    print("Invalid year!")
                    continue

                month = int(input("Birth month (1–12): "))
                if not (1 <= month <= 12):
                    print("Invalid month!")
                    continue

                if month < 7:
                    day = int(input("Birth day (1–31): "))
                    if not (1 <= day <= 31):
                        print("Invalid day!")
                        continue
                else:
                    day = int(input("Birth day (1–30): "))
                    if not (1 <= day <= 30):
                        print("Invalid day!")
                        continue
            except ValueError:
                print("Birth date must be numeric!")
                continue

            birth_date = f"{year}/{month}/{day}"

            user = self.service.create_passenger(
                username, password, first_name, last_name, ph, birth_date
            )

            print("New user was created!")
            return user

    def login(self):
        while True:
            username = input("Enter username (q to quit): ").lower()
            if username == "q":
                return None

            password = input("Enter password: ")

            user = self.service.authenticate(username, password)
            if user:
                print("Login successful!")
                return user

            print("Invalid username or password.")
            try_again = input("Try again? (y/n): ").lower()
            if try_again != "y":
                return None
