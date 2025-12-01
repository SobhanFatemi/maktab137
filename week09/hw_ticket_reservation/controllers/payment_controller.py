from models.payment import PaymentModel


class PaymentController:
    def __init__(self):
        self.service = PaymentModel()

    def pay(self, user):
        tickets = self.service.find_reserved_for_user(user["id"])
        if not tickets:
            print("No reserved tickets!")
            return

        total = 0
        for i, t in enumerate(tickets, 1):
            print(
                f"{i}. Ticket #{t['id']} "
                f"(Travel #{t['travel_id']}) - Price: {t['price']}T"
            )
            total += t["price"]

        print(f"Total: {total}T")

        choice = input("Enter ticket # or 't' for all: ")

        if choice == "t":
            self.service.pay_all(user["id"])
            print("All tickets paid!")
            return

        try:
            idx = int(choice)
        except ValueError:
            print("Invalid.")
            return

        if not (1 <= idx <= len(tickets)):
            print("Invalid ticket.")
            return

        tid = tickets[idx - 1]["id"]
        self.service.pay_one(tid)
        print("Ticket paid!")
