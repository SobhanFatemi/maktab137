<<<<<<< HEAD
import random
import string
from models.user import UserModel
from utils.communication import send_email


def require_not_banned(func):
    def wrapper(self, *args, **kwargs):
        if self.service.is_banned():
            print("You are banned! Do captcha to unlock.")

            if not self.captcha():
                print("Incorrect CAPTCHA!")
                return None  

            self.service.unban()

        return func(self, *args, **kwargs) 
    return wrapper



class AuthController:
    def __init__(self):
        self.service = UserModel()
        self.otp_store = {}

    @require_not_banned
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

            email = input("Please enter your email: ")

            if self.service.email_exists(email):
                print("Email already exists!")
                continue

            if "@" not in email or "." not in email:
                print("Invalid email format!")
                continue

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
                username, password, first_name, last_name, email, ph, birth_date
            )

            print("New user was created!")
            return user
        
    @require_not_banned
    def login(self):
        tries = 0
        while True:
            username = input("Enter username (q to quit): ").lower()
            if username == 'q':
                return None
                
            if self.service.username_exists(username):
                while True:
                    if tries >= 5:
                        self.service.ban()
                        return

                    password = input("Enter password: (q to quit):")
                    
                    if password == 'q':
                        return None
                    user = self.service.authenticate(username, password)
                    if user:
                        print("Login successful!")
                        return user
                
                    tries += 1
                    print("Invalid password.")
                    forgot_password = input("Forgot your password? (y/N): ").lower()

                    if forgot_password == "y":
                        return self.login_via_otp(tries)
                    else:
                        continue
            else:
                print("User does nor exist!")
                continue

    @require_not_banned     
    def login_via_otp(self, tries=0):   
        while True:
            username = input("Enter username (q to quit): ").lower()
            if username == "q":
                return None

            u = UserModel.find_by_username(username)
            if not u:
                print("Username does not exist!")
                continue

            otp = random.randint(100000, 999999)
            self.otp_store[username] = otp

            send_email(u["email"], "Your OTP Code", f"Your OTP is: {otp}")
            while True:
                if tries >= 5:
                    self.service.ban()
                    return
                    
                entered = input("Enter the OTP sent to your email (q to quit): ")
                if entered == 'q':
                    return None

                if entered == str(otp):
                    print("OTP verified! Login successful.")
                    return u
                else:
                    print("Invalid OTP.")
                    tries += 1
                    continue

    @require_not_banned
    def login_with_google(self):
        print("Isn't working yet! sorry :(")
        return
    
    @staticmethod
    def generate_captcha(length=5):

        characters = string.ascii_letters + string.digits
        captcha = ""
        for _ in range(length):
            captcha += random.choice(characters)  
        return captcha


    def captcha(self):
        captcha = self.generate_captcha()
        print("CAPTCHA:", captcha)
        
        user_input = input("Enter the CAPTCHA: ")
        
        if user_input == captcha:
            return True
        else:
            return False
=======
import random
import string
from models.user import UserModel
from utils.communication import send_email


def require_not_banned(func):
    def wrapper(self, *args, **kwargs):
        if self.service.is_banned():
            print("You are banned! Do captcha to unlock.")

            if not self.captcha():
                print("Incorrect CAPTCHA!")
                return None  

            self.service.unban()

        return func(self, *args, **kwargs) 
    return wrapper



class AuthController:
    def __init__(self):
        self.service = UserModel()
        self.otp_store = {}

    @require_not_banned
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

            email = input("Please enter your email: ")

            if self.service.email_exists(email):
                print("Email already exists!")
                continue

            if "@" not in email or "." not in email:
                print("Invalid email format!")
                continue

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
                username, password, first_name, last_name, email, ph, birth_date
            )

            print("New user was created!")
            return user
        
    @require_not_banned
    def login(self):
        tries = 0
        while True:
            username = input("Enter username (q to quit): ").lower()
            if username == 'q':
                return None
                
            if self.service.username_exists(username):
                while True:
                    if tries >= 5:
                        self.service.ban()
                        return

                    password = input("Enter password: (q to quit):")
                    
                    if password == 'q':
                        return None
                    user = self.service.authenticate(username, password)
                    if user:
                        print("Login successful!")
                        return user
                
                    tries += 1
                    print("Invalid password.")
                    forgot_password = input("Forgot your password? (y/N): ").lower()

                    if forgot_password == "y":
                        return self.login_via_otp(tries)
                    else:
                        continue
            else:
                print("User does nor exist!")
                continue

    @require_not_banned     
    def login_via_otp(self, tries=0):   
        while True:
            username = input("Enter username (q to quit): ").lower()
            if username == "q":
                return None

            u = UserModel.find_by_username(username)
            if not u:
                print("Username does not exist!")
                continue

            otp = random.randint(100000, 999999)
            self.otp_store[username] = otp

            send_email(u["email"], "Your OTP Code", f"Your OTP is: {otp}")
            while True:
                if tries >= 5:
                    self.service.ban()
                    return
                    
                entered = input("Enter the OTP sent to your email (q to quit): ")
                if entered == 'q':
                    return None

                if entered == str(otp):
                    print("OTP verified! Login successful.")
                    return u
                else:
                    print("Invalid OTP.")
                    tries += 1
                    continue

    @require_not_banned
    def login_with_google(self):
        print("Isn't working yet! sorry :(")
        return
    
    @staticmethod
    def generate_captcha(length=5):

        characters = string.ascii_letters + string.digits
        captcha = ""
        for _ in range(length):
            captcha += random.choice(characters)  
        return captcha


    def captcha(self):
        captcha = self.generate_captcha()
        print("CAPTCHA:", captcha)
        
        user_input = input("Enter the CAPTCHA: ")
        
        if user_input == captcha:
            return True
        else:
            return False
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
