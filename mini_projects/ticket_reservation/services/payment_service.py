from models.payment import PaymentModel
from models.ticket import TicketModel
from models.travel import TravelModel


class PaymentService:

    def find_reserved_for_user(self, user_id):
        reserved = TicketModel.find_reserved_by_user(user_id)
        results = []

        for t in reserved:
            travel = TravelModel.find_by_id(t["travel_id"])
            price = travel["price"] if travel else 0
            entry = t.copy()
            entry["price"] = price
            results.append(entry)

        return results

    def pay_one(self, ticket_id):
        ticket = TicketModel.find_by_id(ticket_id)
        travel = TravelModel.find_by_id(ticket["travel_id"])
        price = travel["price"]

        PaymentModel.create(ticket["user_id"], ticket["travel_id"], price)

        all_tickets = TicketModel.load_all()
        for t in all_tickets:
            if t["id"] == ticket_id:
                t["status"] = "paid"
                break

        TicketModel.save_all(all_tickets)

    def pay_all(self, user_id):
        for t in TicketModel.find_reserved_by_user(user_id):
            self.pay_one(t["id"])
