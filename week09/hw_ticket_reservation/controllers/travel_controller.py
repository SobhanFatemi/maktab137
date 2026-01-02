<<<<<<< HEAD
from models.travel import TravelModel



class TravelController:
    def __init__(self):
        self.service = TravelModel()

    def search_travel(self):
        origin = input("Please enter your current city: ").capitalize()

        travels = self.service.search_available(origin)

        if not travels:
            print(f"No available travels from '{origin}'!")
            return []

        print("Available travels:")
        for i, t in enumerate(travels, 1):
            print(
                f"{i}. {t['origin']} → {t['destination']} at {t['starting_time']} "
                f"- Price: {t['price']}T"
            )

        return travels

    def create_travel(self):
        origin = input("Origin: ").capitalize()
        destination = input("Destination: ").capitalize()
        starting_time = input("Start (YYYY-MM-DD HH:MM): ")

        try:
            duration = int(input("Duration in minutes: "))
            max_p = int(input("Max passengers: "))
            seat_count = int(input("How many available seats: "))
        except ValueError:
            print("Invalid number.")
            return

        seats = []
        for i in range(seat_count):
            seats.append(input(f"Seat #{i+1}: "))

        try:
            price = int(input("Price (Toman): "))
        except ValueError:
            print("Invalid price.")
            return

        status = "available" if seats else "full"

        self.service.create(
            origin=origin,
            destination=destination,
            starting_time=starting_time,
            duration=duration,
            max_passengers=max_p,
            available_seats=seats,
            price=price,
            status=status,
        )

        print("Travel created!")

    def edit_travel(self):
        travel_id = input("Enter travel id: ")
        if not travel_id.isdigit():
            print("Invalid id!")
            return

        travel = self.service.find(int(travel_id))
        if not travel:
            print("Travel not found!")
            return

        while True:
            print(
                "\n1- Change Origin\n2- Change destination\n3- Change starting time\n"
                "4- Change duration\n5- Change max passengers\n6- Edit available seats\n"
                "7- Change price\n8- Save changes\n9- Change travel status\n10- Quit"
            )
            choice = input("Your choice: ")

            if choice == "1":
                travel["origin"] = input("New origin: ").capitalize()

            elif choice == "2":
                travel["destination"] = input("New destination: ").capitalize()

            elif choice == "3":
                travel["starting_time"] = input("New time: ")

            elif choice == "4":
                try:
                    travel["duration"] = int(input("New duration: "))
                except ValueError:
                    print("Invalid!")

            elif choice == "5":
                try:
                    travel["max_passengers"] = int(input("New max: "))
                except ValueError:
                    print("Invalid!")

            elif choice == "6":
                seats = travel["available_seats"]
                print("1- Add\n2- Remove\n3- Back")
                sub = input("Choice: ")

                if sub == "1":
                    seat = input("Seat: ")
                    seats.append(seat)

                elif sub == "2":
                    for i, s in enumerate(seats, 1):
                        print(i, s)
                    try:
                        rm = int(input("Remove #"))
                        seats.pop(rm - 1)
                    except:
                        print("Invalid seat.")

            elif choice == "7":
                try:
                    travel["price"] = int(input("New price: "))
                except ValueError:
                    print("Invalid price.")

            elif choice == "8":
                self.service.save()
                print("Saved.")

            elif choice == "9":
                print("1- Available\n2- Full\n3- Canceled")
                ch = input("New status: ")
                if ch == "1":
                    travel["status"] = "available"
                elif ch == "2":
                    travel["status"] = "full"
                elif ch == "3":
                    travel["status"] = "canceled"
                else:
                    print("Invalid.")

            elif choice == "10":
                break
=======
from models.travel import TravelModel



class TravelController:
    def __init__(self):
        self.service = TravelModel()

    def search_travel(self):
        origin = input("Please enter your current city: ").capitalize()

        travels = self.service.search_available(origin)

        if not travels:
            print(f"No available travels from '{origin}'!")
            return []

        print("Available travels:")
        for i, t in enumerate(travels, 1):
            print(
                f"{i}. {t['origin']} → {t['destination']} at {t['starting_time']} "
                f"- Price: {t['price']}T"
            )

        return travels

    def create_travel(self):
        origin = input("Origin: ").capitalize()
        destination = input("Destination: ").capitalize()
        starting_time = input("Start (YYYY-MM-DD HH:MM): ")

        try:
            duration = int(input("Duration in minutes: "))
            max_p = int(input("Max passengers: "))
            seat_count = int(input("How many available seats: "))
        except ValueError:
            print("Invalid number.")
            return

        seats = []
        for i in range(seat_count):
            seats.append(input(f"Seat #{i+1}: "))

        try:
            price = int(input("Price (Toman): "))
        except ValueError:
            print("Invalid price.")
            return

        status = "available" if seats else "full"

        self.service.create(
            origin=origin,
            destination=destination,
            starting_time=starting_time,
            duration=duration,
            max_passengers=max_p,
            available_seats=seats,
            price=price,
            status=status,
        )

        print("Travel created!")

    def edit_travel(self):
        travel_id = input("Enter travel id: ")
        if not travel_id.isdigit():
            print("Invalid id!")
            return

        travel = self.service.find(int(travel_id))
        if not travel:
            print("Travel not found!")
            return

        while True:
            print(
                "\n1- Change Origin\n2- Change destination\n3- Change starting time\n"
                "4- Change duration\n5- Change max passengers\n6- Edit available seats\n"
                "7- Change price\n8- Save changes\n9- Change travel status\n10- Quit"
            )
            choice = input("Your choice: ")

            if choice == "1":
                travel["origin"] = input("New origin: ").capitalize()

            elif choice == "2":
                travel["destination"] = input("New destination: ").capitalize()

            elif choice == "3":
                travel["starting_time"] = input("New time: ")

            elif choice == "4":
                try:
                    travel["duration"] = int(input("New duration: "))
                except ValueError:
                    print("Invalid!")

            elif choice == "5":
                try:
                    travel["max_passengers"] = int(input("New max: "))
                except ValueError:
                    print("Invalid!")

            elif choice == "6":
                seats = travel["available_seats"]
                print("1- Add\n2- Remove\n3- Back")
                sub = input("Choice: ")

                if sub == "1":
                    seat = input("Seat: ")
                    seats.append(seat)

                elif sub == "2":
                    for i, s in enumerate(seats, 1):
                        print(i, s)
                    try:
                        rm = int(input("Remove #"))
                        seats.pop(rm - 1)
                    except:
                        print("Invalid seat.")

            elif choice == "7":
                try:
                    travel["price"] = int(input("New price: "))
                except ValueError:
                    print("Invalid price.")

            elif choice == "8":
                self.service.save()
                print("Saved.")

            elif choice == "9":
                print("1- Available\n2- Full\n3- Canceled")
                ch = input("New status: ")
                if ch == "1":
                    travel["status"] = "available"
                elif ch == "2":
                    travel["status"] = "full"
                elif ch == "3":
                    travel["status"] = "canceled"
                else:
                    print("Invalid.")

            elif choice == "10":
                break
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
