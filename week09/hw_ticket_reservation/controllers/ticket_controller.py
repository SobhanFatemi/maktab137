from models.ticket import TicketModel


class TicketController:
    def __init__(self):
        self.service = TicketModel()

    def reserve_ticket(self, user, travels):
        try:
            idx = int(input("Select travel #: "))
        except ValueError:
            print("Invalid input!")
            return

        if not (1 <= idx <= len(travels)):
            print("Invalid travel number!")
            return

        travel = travels[idx - 1]

        seats = travel["available_seats"]
        if not seats:
            print("No seats available!")
            return

        print("Available seats:")
        for i, s in enumerate(seats, 1):
            print(i, s)

        try:
            seat_idx = int(input("Select seat #: "))
        except ValueError:
            print("Invalid!")
            return

        if not (1 <= seat_idx <= len(seats)):
            print("Invalid seat!")
            return

        seat = seats[seat_idx - 1]
        ticket = self.service.reserve(user["id"], travel["id"], seat)

        print(f"Ticket reserved! Ticket ID: {ticket['id']}")

    def users_in_travel(self):
        try:
            travel_id = int(input("Travel id: "))
        except ValueError:
            print("Invalid id!")
            return

        users = self.service.find_by_travel(travel_id)
        if not users:
            print("No users found.")
            return

        for t in users:
            print(f"User #{t['user_id']} - {t['status']}")
