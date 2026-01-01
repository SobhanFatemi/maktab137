import bcrypt
from datetime import datetime
import json
import os

USERS_PATH = "users.json"
TRAVELS_PATH = "travels.json"
TICKETS_PATH = "tickets.json"
PAYMENTS_PATH = "payments.json"

def main_menu():
    active_user = None
    PassengerUser.load_last_id(USERS_PATH)
    AdminUser.load_last_id(USERS_PATH)
    Travel.load_last_id(TRAVELS_PATH)
    Ticket.load_last_id(TICKETS_PATH)
    Payment.load_last_id(PAYMENTS_PATH)

    while True:
        if active_user and active_user.role == "passenger":
            first_choice = input("Please enter your desired chocie:\n1- Search travels\n2- Pay for reserved tickets\n3- Logout\n4- Quit\nYour choice: ")

            if first_choice == '1':
                available_tickets = search_travel()
                if available_tickets:
                    user_ticket = ticket_reservation(active_user, available_tickets)
                    print(f"Ticket reserved!\nTicket ID: {user_ticket.id}")

            elif first_choice == '2':
                    pay(active_user)

            elif first_choice == '3':
                make_sure = input("Are you sure you want to logout? (y/n): ")

                if make_sure == 'y':
                    active_user = None
                    continue
            elif first_choice == '4':
                print("Quitting...")
                break

            else:
                print("Invalid input!")
        
        elif active_user and active_user.role == "admin":
            first_choice = input("Please enter your desired chocie:\n1- Search travels\n2- Pay for reserved tickets\n3- Create new travel\n4- Edit Travel\n5- Passenger IDs in a travel\n6- Make a user admin\n7- Logout\n8- Quit\nYour choice: ")

            if first_choice == '1':
                available_tickets = search_travel()
                if available_tickets:
                    user_ticket = ticket_reservation(active_user, available_tickets)
                    print(f"Ticket reserved!\nTicket ID: {user_ticket.id}")

            elif first_choice == '2':
                pay(active_user)

            elif first_choice == '3':
                create_travel()

            elif first_choice == '4':
                edit_travel()

            elif first_choice == '5':
                search_users_in_travel()

            elif first_choice == '6':
                make_admin()

            elif first_choice == '7':
                make_sure = input("Are you sure you want to logout? (y/n): ")

                if make_sure == 'y':
                    active_user = None
                    continue
            elif first_choice == '8':
                print("Quitting...")
                break

        else:
            first_choice = input("Please enter your desired chocie:\n1- Sign in\n2- Log in\n3- Quit\nYour choice: ")

            if first_choice == '1':
                active_user = sign_in()

            elif first_choice == '2':
                active_user = login()
                continue
            
            elif first_choice == '3':
                break

            else:
                print("Invalid Input!")
                continue

def sign_in():
    while True:
        username = input("Please enter your username (q to quit): ").lower()
        if username == "q":
            break

        if len(username) < 5:
            print("Username must have at least 5 charecters!")
            continue

        if len(username) > 15:
            print("Username can not have more than 15 charecters!")
            continue

        User.ensure_file()
        username = User.check_username(username)

        if not username:
            print("Username already exists!")
            continue

        password = input("Please enter you password: ")
        if len(password) < 6:
            print("Password must be more than 6 characters!")
            continue
        elif len(password) > 15:
            print("Password must be less than 15 characters!")
            continue

        first_name = input("Please enter your first name: ")

        last_name = input("Please enter your last name: ")

        try:
            ph_number = int(input("Please enter your phone number: "))
        except ValueError:
            print("Phone can not include characters!")
            continue
        try:
            birth_year = int(input("Please enter the year you were born: (1925-2010): "))
            if birth_year < 1925 or birth_year > 2010:
                print("Invalid birth year!")
                continue

            birth_month = int(input("Please enter the month you were born: (1-12): "))
            if birth_month < 1 or birth_month > 12:
                print("Invalid birth month!")
                continue
                        
            if 0 < birth_month < 7:
                birth_day = int(input("Please enter the day you were born: (1-31): "))
                if birth_day < 1 or birth_day > 31:
                    print("Invalid birth day!")
                    continue
            else:
                birth_day = int(input("Please enter the day you were born: (1-30): "))
                if birth_day < 1 or birth_day > 30:
                    print("Invalid birth day!")
                    continue
        except ValueError:
            print("Should only include integers!")


        birth_date = f"{birth_year}/{birth_month}/{birth_day}"

        print("New user was created!")

        return PassengerUser(username, password, first_name, last_name, ph_number, birth_date)   

def login():
    while True:
            found = False
            username = input("Please enter your username (q to quit): ").lower()
            if username == "q":
                break

            if len(username) < 5:
                print("Username must have at least 5 charecters!")
                continue

            if len(username) > 15:
                print("Username can not have more than 15 charecters!")
                continue

            password = input("Please enter your password: ")
            if len(password) < 6:
                print("Password must be more than 6 characters!")
                continue
            elif len(password) > 15:
                print("Password must be less than 15 characters!")
                continue
    
            with open(USERS_PATH, 'r') as file:
                users = json.load(file)

            for user in users:
                if username == user["username"]:
                    found = True

                    if user["role"] == "admin":
                        obj = AdminUser.from_dict(user)
                    else:
                        obj = PassengerUser.from_dict(user)


                    if obj.check_password(password):
                        print("Login successful!")
                        return obj
                    else:
                        print("Wrong password!")
                        try_again = input("Try again? (y/n): ").lower()
                        if try_again == 'y':
                            continue
                        return None
            if not found:
                print("User does not exist!")
                try_again = input("Try again? (y/n): ").lower()
                if try_again == 'y':
                    continue
                return None

    print(f"'{username}' not found!")
    return None

def search_travel():
    while True:
        available_travels = []
        origin = input("Please enter your current city: ").capitalize()
        with open(TRAVELS_PATH, 'r') as file:
            travels = json.load(file)
            for travel in travels:
                if origin == travel["origin"] and travel["status"] == "available":
                    available_travels.append(travel)
        if available_travels:
            print("All available travels:")
            for i, travel in enumerate(available_travels):
                print(f"{i+1}. '{travel["origin"]}' to '{travel["destination"]}' at {travel["starting_time"]} - Price: {travel["price"]}T")

            reserve_tickets = input("Do you want to buy tickets? (y/n): ").lower()

            if reserve_tickets == 'y':
                return available_travels
            
            elif reserve_tickets == 'n':
                keep_searching = input("Do you want to keep searching? (y/n): ").lower()

            else:
                print("Invalid input!")
                continue

            if keep_searching == 'y':
                continue

            elif keep_searching == 'n':
                break

            else:
                print("Invalid input!")
                continue
            
        else:
            print(f"No available travels from '{origin}'!")
            try_again = input("Try again? (y/n): ").lower()
            if try_again == 'y':
                continue
            break

def ticket_reservation(active_user, available_travels):
    while True:
        try:
            travel_index = int(input("Please enter the travel you want to reserve the tickets for: "))
        except ValueError:
            print("You need to enter the number of the travel you want to reserve the ticket for!")
            try_again = input("Try again? (y/n): ").lower()
            if try_again == 'y':
                continue
            break
        if travel_index > len(available_travels):
            print("That travel number doesn't exist!")
            try_again = input("Try again? (y/n): ").lower()
            if try_again == 'y':
                continue
            break
        
        
        chosen_travel = available_travels[travel_index - 1]
        print("Available seats: ")
        if chosen_travel["available_seats"]:
            for i, seat in enumerate(chosen_travel["available_seats"]):
                print(f"{i+1}. '{seat}'")
            
            try:
                seat_index = int(input("Please enter the seat you want to reserve the tickets for: "))
            except ValueError:
                print("You need to enter the number of the seat you want to reserve the ticket for!")
                try_again = input("Try again? (y/n): ").lower()
                if try_again == 'y':
                    continue
                break
            if seat_index > len(chosen_travel["available_seats"]):
                print("That seat number doesn't exist!")
                try_again = input("Try again? (y/n): ").lower()
                if try_again == 'y':
                    continue
                break
            


            chosen_seat = chosen_travel["available_seats"][seat_index - 1]

            with open(TRAVELS_PATH, 'r') as file:
                travels = json.load(file)

            for travel in travels:
                if travel["id"] == chosen_travel["id"]:
                    travel["available_seats"].remove(chosen_seat)
                    if not travel["available_seats"]:
                        travel["status"] = "full"

            with open(TRAVELS_PATH, 'w') as file:
                json.dump(travels, file, indent=4)

            new_ticket = Ticket(active_user.id, chosen_travel["id"], chosen_seat, "reserved")
            
            return new_ticket
        else:
            print("No seats available for this travel!")
            try_again = input("Try again? (y/n): ").lower()
            if try_again == 'y':
                continue
            break

def pay(active_user):
    reserved_tickets = []
    with open(TICKETS_PATH, 'r') as file:
        tickets = json.load(file)

    with open(TRAVELS_PATH, 'r') as file:
        travels = json.load(file)

    for ticket in tickets:
        if ticket["user_id"] == active_user.id and ticket["status"] == "reserved":
            reserved_tickets.append(ticket)

    if not reserved_tickets:
        print("No tickets were reserved!")
        return
    
    total_price = 0
    for i, ticket in enumerate(reserved_tickets):
        for travel in travels:
            if travel["id"] == ticket["travel_id"]:
                total_price += travel["price"]
                current_travel = travel
        print(f"{i+1}.Ticket ID: #{ticket["id"]} - Travel ID: #{ticket["travel_id"]} - Price: {current_travel["price"]}T")

    print(f"Total: {total_price}T")

    while True:
        payout_choice = input("Enter the ticket to payout or 't' to pay all: ")
        if payout_choice == 't':
            for ticket in tickets:
                for reserved_ticket in reserved_tickets:
                    if ticket["id"] == reserved_ticket["id"]:
                        for travel in travels:
                            if travel["id"] == ticket["travel_id"]:
                                price = travel["price"]
                        Payment(ticket["user_id"], ticket["travel_id"], price, "successful")
                        ticket["status"] = "paid"
            break
        else:
            try:
                int_payout_choice = int(payout_choice)
            except ValueError:
                print("Invalid input! (none int)")
                continue

            if int_payout_choice > len(reserved_tickets):
                print("Invalid input! (out of range)")
                continue

            chosen_ticket = reserved_tickets[int_payout_choice - 1]  
            
            for ticket in tickets:
                if ticket["id"] == chosen_ticket["id"]:
                    for travel in travels:
                        if travel["id"] == ticket["travel_id"]:
                            price = travel["price"]
                    Payment(ticket["user_id"], ticket["travel_id"], price, "successful")
                    ticket["status"] = "paid"
            break

    with open(TICKETS_PATH, 'w') as file:
        json.dump(tickets, file, indent=4)
        print("Payout was successful!")

def create_travel():
    while True:
        available_seats_list = []

        origin = input("Please enter the origin city: ").capitalize()

        destination = input("Please enter the destination city: ").capitalize()

        starting_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")

        try:
            datetime.strptime(starting_time, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD HH:MM.")
            continue

        try:
            duration = int(input("Please enter travel duration in minutes: "))
        except ValueError:
            print("Please enter the duration in minutes <number>!")
            continue

        try:
            max_passengers = int(input("Please enter the maximum number of passenger seats: "))
        except ValueError:
            print("Please enter the maximum <number>!")
            continue
        
        try:
            available_seats = int(input("Please enter how many available seats you want to enter: "))
        except ValueError:
            print("Please enter the <number>!")
            continue

        for i, _ in enumerate(range(available_seats)):
            seat_number = input(f"#{i+1}. Please enter the seat number: ")
            available_seats_list.append(seat_number)

        try:
            price = int(input("Please enter the price of this travel: "))
        except ValueError:
            print("Please enter price in Tomans <number>!")
            continue
        
        Travel(origin, destination, starting_time, duration, max_passengers, available_seats_list, price, "available" if available_seats_list else "full")
        print("Travel Created!")
        break
        
def edit_travel():
    while True:
        found = False
        active_travel = None

        travel_id_str = input("Please enter the travel id (q to quit): ")
        if travel_id_str == 'q':
            break
        try:
            travel_id = int(travel_id_str)
        except ValueError:
            print("You need to enter the id in <number>!")
            continue

        with open(TRAVELS_PATH, 'r') as file:
            travels = json.load(file)

        for travel in travels:
            if travel_id == travel["id"]:
                active_travel = travel
                found = True
                break
        
        if not found:
            print("Travel not found!")
            continue

        while True:
            first_choice = input("Please enter your desired choice:\n1- Change Origin\n2- Change destination\n3- Change starting time\n4- Change duration\n5- Change max passangers\n6- Edit available seats\n7- Change price\n8- Save changes to file\n9- Change travel status\n10- Quit\nYour choice: ")

            if first_choice == '1':
                origin = input("Please enter the origin city: ").capitalize()
                active_travel["origin"] = origin
                print("Origin changed successfully!")
                continue

            elif first_choice == '2':
                destination = input("Please enter the destination city: ").capitalize()
                active_travel["destination"] = destination
                print("Destination changed successfully!")
                continue
            
            elif first_choice == '3':
                starting_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                try:
                    datetime.strptime(starting_time, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Invalid format! Please use YYYY-MM-DD HH:MM.")
                    continue  
                active_travel["starting_time"] = starting_time
                print("Starting time changed successfully!")
                continue

            elif first_choice == '4':
                try:
                    duration = int(input("Please enter travel duration in minutes: "))
                except ValueError:
                    print("Please enter the duration in minutes <number>!")
                    continue
                active_travel["duration"] = duration
                print("Duration changed successfully!")
                continue

            elif first_choice == '5':
                try:
                    max_passengers = int(input("Please enter the maximum number of passenger seats: "))
                except ValueError:
                    print("Please enter the maximum <number>!")
                    continue
                active_travel["max_passengers"] = max_passengers
                print("Max passengers changed successfully!")
                continue
            
            elif first_choice == '6':
                while True:
                    second_choice = input("Please enter your desired choice:\n1- Add new seats\n2- Remove a seat\n3- Quit\nYour choice: ")

                    if second_choice == '1':
                        try:
                            available_seats = int(input("Please enter how many available seats you want to enter: "))
                        except ValueError:
                            print("Please enter the <number>!")
                            continue

                        for i, _ in enumerate(range(available_seats)):
                            seat_number = input(f"#{i+1}. Please enter the seat number: ")
                            active_travel["available_seats"].append(seat_number)
                            print(f"'{seat_number}' was added successfully!")
                    
                    elif second_choice == '2':
                        if active_travel["available_seats"]:
                            for i, available_seat in enumerate(active_travel["available_seats"]):
                                print(f"{i+1}. {available_seat}")
                            try:
                                seat_to_remove = int(input(f"Please enter the seat you want to remove (1, {len(active_travel["available_seats"])}): "))
                            except ValueError:
                                print("Please enter the <number>!")
                                continue
                            if seat_to_remove > len(active_travel["available_seats"]):
                                print("That seat doesn't exist!")
                                continue
                            print(f"Removing '{active_travel["available_seats"][seat_to_remove - 1]}'...")
                            del active_travel["available_seats"][seat_to_remove - 1]

                        else:
                            print("No seats available for this travel to remove!")
                            continue
                    elif second_choice == '3':
                        break

                    else:
                        print("Invalid input")
                        continue
            elif first_choice == '7':
                try:
                    price = int(input("Please enter the price of this travel: "))
                except ValueError:
                    print("Please enter price in Tomans <number>!")
                    continue

                active_travel["price"] = price
                print("Price changed successfully!")
                continue

            elif first_choice == '8':
                with open(TRAVELS_PATH, 'w') as file:
                    json.dump(travels, file, indent=4)
                print("Changes saved!")

            elif first_choice == '9':
                while True:
                    status = input("Please enter the status:\n1- Available\n2- Full\n3- Canceled\n4- Quit")

                    if status == '1':
                        if not active_travel["available_seats"]:
                            print("There are no seats available!")
                            continue
                        active_travel["status"] = "available"
                        print("Status changed successfully!")
                        continue

                    elif status == '2':
                        if active_travel["available_seats"]:
                            make_sure = input("These seats are still available do you still want to turn this travel's status to full? (y/n): ")
                            for i, available_seat in enumerate(active_travel["available_seats"]):
                                print(f"{i+1}. {available_seat}")

                            if make_sure == 'n':
                                continue

                        active_travel["status"] = "full"
                        print("Status changed successfully!")
                        continue

                    elif status == '3':
                        active_travel["status"] = "canceled"
                        print("Status changed successfully!")
                        continue

                    elif status == '4':
                        break

                    else:
                        print("Invalid input!")
                        continue
                

            elif first_choice == '10':
                break

            else:
                print("Invalid input!")
                continue

def search_users_in_travel():
    while True:
        found = False

        travel_id_str = input("Please enter the travel id (q to quit): ")
        if travel_id_str == 'q':
            break
        try:
            travel_id = int(travel_id_str)
        except ValueError:
            print("You need to enter the id in <number>!")
            continue

        with open(TRAVELS_PATH, 'r') as file:
            travels = json.load(file)

        for travel in travels:
            if travel_id == travel["id"]:
                found = True
                break
        
        if not found:
            print("Travel not found!")
            continue
        
        with open(TICKETS_PATH, 'r') as file:
            tickets = json.load(file)

        print(f"User IDs for travel #{travel_id}")
        for ticket in tickets:
            if ticket["travel_id"] == travel_id:
                print(f"#{ticket['user_id']}: {ticket['status'].capitalize()}")
     
def make_admin():
    while True:
        user_to_admin = None
        found = False

        user_id_str = input("Please enter the user id you want to make admin (q to quit): ")
        if user_id_str == 'q':
            break
        try:
            user_id = int(user_id_str)
        except ValueError:
            print("You need to enter the id in <number>!")
            continue

        with open(USERS_PATH, 'r') as file:
            users = json.load(file)

        for user in users:
            if user_id == user["id"]:
                user_to_admin = user
                found = True
                break
        
        if not found:
            print("User not found!")
            continue
        
        if user_to_admin["role"] == "admin":
            print(f"'{user["username"]}' is already an admin!")
            continue

        make_sure = input(f"Are you sure you want to make '{user["username"]}' admin? (y/n): ")

        if make_sure == 'y':
            user_to_admin["role"] = "admin"
            with open(USERS_PATH, 'w') as file:
                json.dump(users, file, indent=4)
            print(f"'{user["username"]}' is now an admin!")

        else:
            continue


class User:
    def __init__(self, username: str, password: str, first_name: str, last_name: str, ph_number: int, birth_date: str):
        User.ensure_file()
        self.password_hash = self.hash_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.ph_number = ph_number
        self.birth_date = birth_date
        self.username = self.check_username(username)
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def ensure_file():
        if not os.path.exists(USERS_PATH):
            with open(USERS_PATH, "w") as file:
                json.dump([], file)

    @classmethod
    def from_dict(cls, data):
        obj = cls.__new__(cls)

        obj.username = data["username"]
        obj.password_hash = data["password_hash"]
        obj.first_name = data["first_name"]
        obj.last_name = data["last_name"]
        obj.ph_number = data["ph_number"]
        obj.birth_date = data["birth_date"]
        obj.role = data["role"]
        obj.id = data["id"]
        obj.created_at = data["created_at"]

        return obj
    
    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash.encode("utf-8"))
    
    @staticmethod
    def check_username(username):
        with open(USERS_PATH, 'r') as file:
            users = json.load(file)
            for user in users:
                if username == user["username"]:
                    return None
        return username         
    
    def save_to_file(self):
        with open(USERS_PATH, "r") as file:
            users = json.load(file)

        data = {
            "id": self.id,
            "role": self.role,
            "username": self.username,
            "password_hash": self.password_hash,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "ph_number": self.ph_number,
            "birth_date": self.birth_date,
            "created_at": self.created_at
        }

        users.append(data)
        with open(USERS_PATH, "w") as file:
            json.dump(users, file, indent=4)


class AdminUser(User):
    id = 100100
    def __init__(self, username: str, password: str, first_name: str, last_name: str, ph_number: int, birth_date: str):
        super().__init__(username, password, first_name, last_name, ph_number, birth_date)
        self.id = AdminUser.id
        AdminUser.id += 1
        self.role = "admin"
        self.save_to_file()

    @classmethod
    def load_last_id(cls, path):
        if not os.path.exists(path):
            return
        with open(path, "r") as file:
            data = json.load(file)
            if data:
                cls.id = max(item["id"] for item in data) + 1


class PassengerUser(User):
    id = 200100
    def __init__(self, username: str, password: str, first_name: str, last_name: str, ph_number: int, birth_date: str):
        super().__init__(username, password, first_name, last_name, ph_number, birth_date)
        self.id = PassengerUser.id
        PassengerUser.id += 1
        self.role = "passenger"
        self.save_to_file()

    @classmethod
    def load_last_id(cls, path):
        if not os.path.exists(path):
            return
        with open(path, "r") as file:
            data = json.load(file)
            if data:
                cls.id = max(item["id"] for item in data) + 1


class Travel:
    id = 300100
    def __init__(self, origin: str, destination: str, starting_time: str, duration: int, max_passengers: int, available_seats: list, price: int, status: str):
        Travel.ensure_file()

        self.id = Travel.id
        Travel.id += 1
        self.origin = origin
        self.destination = destination
        self.starting_time = starting_time
        self.duration = duration
        self.max_passengers = max_passengers
        self.available_seats = available_seats
        self.price = price
        self.status = status
        self.save_to_file()

    @staticmethod
    def ensure_file():
        if not os.path.exists(TRAVELS_PATH):
            with open(TRAVELS_PATH, "w") as file:
                json.dump([], file)

    def save_to_file(self):
        with open(TRAVELS_PATH, "r") as file:
            users = json.load(file)

        data = {
            "id": self.id,
            "origin": self.origin,
            "destination": self.destination,
            "starting_time": self.starting_time,
            "duration": self.duration,
            "max_passengers": self.max_passengers,
            "available_seats": self.available_seats,
            "price": self.price,
            "status": self.status
        }

        users.append(data)
        with open(TRAVELS_PATH, "w") as file:
            json.dump(users, file, indent=4)

    @classmethod
    def load_last_id(cls, path):
        if not os.path.exists(path):
            return
        with open(path, "r") as file:
            data = json.load(file)
            if data:
                cls.id = max(item["id"] for item in data) + 1


class Ticket:
    id = 400100
    def __init__(self, user_id: int, travel_id: int, seat_number: str, status: str):
        Ticket.ensure_file()
        self.id = Ticket.id
        Ticket.id += 1
        self.user_id = user_id
        self.travel_id = travel_id
        self.seat_number = seat_number
        self.status = status
        self.save_to_file()

    @staticmethod
    def ensure_file():
        if not os.path.exists(TICKETS_PATH):
            with open(TICKETS_PATH, "w") as file:
                json.dump([], file)

    def save_to_file(self):
        with open(TICKETS_PATH, "r") as file:
            users = json.load(file)

        data = {
            "id": self.id,
            "user_id": self.user_id,
            "travel_id": self.travel_id,
            "seat_number": self.seat_number,
            "status": self.status,
        }

        users.append(data)
        with open(TICKETS_PATH, "w") as file:
            json.dump(users, file, indent=4)

    @classmethod
    def load_last_id(cls, path):
        if not os.path.exists(path):
            return
        with open(path, "r") as file:
            data = json.load(file)
            if data:
                cls.id = max(item["id"] for item in data) + 1


class Payment:
    id = 500100
    def __init__(self, user_id: int, travel_id: int, price: int, status: str):
        Payment.ensure_file()

        self.id = Payment.id
        Payment.id += 1
        self.user_id = user_id
        self.travel_id = travel_id
        self.price = price
        self.status = status
        self.save_to_file()

    @staticmethod
    def ensure_file():
        if not os.path.exists(PAYMENTS_PATH):
            with open(PAYMENTS_PATH, "w") as file:
                json.dump([], file)

    def save_to_file(self):
        with open(PAYMENTS_PATH, "r") as file:
            users = json.load(file)

        data = {
            "id": self.id,
            "user_id": self.user_id,
            "travel_id": self.travel_id,
            "price": self.price,
            "status": self.status,
        }

        users.append(data)
        with open(PAYMENTS_PATH, "w") as file:
            json.dump(users, file, indent=4)

    @classmethod
    def load_last_id(cls, path):
        if not os.path.exists(path):
            return
        with open(path, "r") as file:
            data = json.load(file)
            if data:
                cls.id = max(item["id"] for item in data) + 1



main_menu()
