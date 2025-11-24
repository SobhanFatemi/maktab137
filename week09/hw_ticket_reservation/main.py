from controllers.auth_controller import AuthController
from controllers.travel_controller import TravelController
from controllers.ticket_controller import TicketController
from controllers.admin_controller import AdminController
from controllers.payment_controller import PaymentController
from utils.file_utils import ensure_file
from config import USERS_PATH, TRAVELS_PATH, TICKETS_PATH, PAYMENTS_PATH

def main():
    auth = AuthController()
    travel_ctrl = TravelController()
    ticket_ctrl = TicketController()
    admin_ctrl = AdminController()
    payment_ctrl = PaymentController()

    ensure_file(USERS_PATH, [])
    ensure_file(TRAVELS_PATH, [])
    ensure_file(TICKETS_PATH, [])
    ensure_file(PAYMENTS_PATH, [])

    active_user = None

    while True:

        if active_user and active_user["role"] == "passenger":
            print(
                "\nPlease enter your choice:\n"
                "1- Search travels\n"
                "2- Pay for reserved tickets\n"
                "3- Logout\n"
                "4- Quit\n"
            )
            choice = input("Your choice: ")

            if choice == "1":
                available = travel_ctrl.search_travel()
                if available:
                    ticket_ctrl.reserve_ticket(active_user, available)

            elif choice == "2":
                payment_ctrl.pay(active_user)

            elif choice == "3":
                active_user = None
                continue

            elif choice == "4":
                print("Quitting...")
                break

            else:
                print("Invalid input!")

        elif active_user and active_user["role"] == "admin":
            print(
                "\nPlease enter your choice:\n"
                "1- Search travels\n"
                "2- Pay for reserved tickets\n"
                "3- Create new travel\n"
                "4- Edit travel\n"
                "5- Passenger IDs in a travel\n"
                "6- Make a user admin\n"
                "7- Logout\n"
                "8- Quit\n"
            )
            choice = input("Your choice: ")

            if choice == "1":
                available = travel_ctrl.search_travel()
                if available:
                    ticket_ctrl.reserve_ticket(active_user, available)

            elif choice == "2":
                payment_ctrl.pay(active_user)

            elif choice == "3":
                travel_ctrl.create_travel()

            elif choice == "4":
                travel_ctrl.edit_travel()

            elif choice == "5":
                ticket_ctrl.users_in_travel()

            elif choice == "6":
                admin_ctrl.make_admin()

            elif choice == "7":
                active_user = None
                continue

            elif choice == "8":
                print("Quitting...")
                break

            else:
                print("Invalid input!")

        else:
            print(
                "\nPlease enter your choice:\n"
                "1- Sign in\n"
                "2- Log in\n"
                "3- Log in with One time password\n" 
                "4- Log in with Google\n"
            )
            choice = input("Your choice: ")

            if choice == "1":
                active_user = auth.sign_in()

            elif choice == "2":
                active_user = auth.login()

            elif choice == "3":
                active_user = auth.login_via_otp()

            elif choice == "4":
                active_user = auth.login_with_google()

            else:
                print("Invalid input!")


if __name__ == "__main__":
    main()
