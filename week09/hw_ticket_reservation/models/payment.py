import os
from utils.file_utils import load_json, save_json
from utils.id_counters import payment_id
from config import PAYMENTS_PATH
from models.ticket import TicketModel
from models.travel import TravelModel


class PaymentModel:

    @staticmethod
    def load_all():
        return load_json(PAYMENTS_PATH)

    @staticmethod
    def save_all(data):
        save_json(PAYMENTS_PATH, data)

    @staticmethod
    def create(user_id, travel_id, price):
        global payment_id
        payments = load_json(PAYMENTS_PATH)

        data = {
            "id": payment_id,
            "user_id": user_id,
            "travel_id": travel_id,
            "price": price,
            "status": "successful"
        }

        payments.append(data)
        save_json(PAYMENTS_PATH, payments)
        payment_id += 1
        return data
    
    @staticmethod
    def find_reserved_for_user(user_id):
        reserved = TicketModel.find_reserved_by_user(user_id)
        results = []

        for t in reserved:
            travel = TravelModel.find(t["travel_id"])
            price = travel["price"] if travel else 0
            entry = t.copy()
            entry["price"] = price
            results.append(entry)

        return results
    
    @staticmethod
    def pay_one(ticket_id):
        ticket = TicketModel.find_by_id(ticket_id)
        travel = TravelModel.find(ticket["travel_id"])
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