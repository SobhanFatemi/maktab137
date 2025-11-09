import os
from utils.file_utils import load_json, save_json
from utils.id_counters import payment_id
from config import PAYMENTS_PATH


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