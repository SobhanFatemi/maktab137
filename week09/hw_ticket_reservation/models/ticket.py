<<<<<<< HEAD
import os
from utils.file_utils import load_json, save_json
from utils.id_counters import ticket_id
from config import TICKETS_PATH, TRAVELS_PATH


class TicketModel:

    @staticmethod
    def load_all():
        return load_json(TICKETS_PATH)

    @staticmethod
    def save_all(data):
        save_json(TICKETS_PATH, data)

    @staticmethod
    def find_reserved_by_user(uid):
        return [
            t for t in load_json(TICKETS_PATH)
            if t.get("user_id") == uid and t.get("status") == "reserved"
        ]

    @staticmethod
    def find_by_id(tid):
        for t in load_json(TICKETS_PATH):
            if t.get("id") == tid:
                return t
        return None

    @staticmethod
    def find_by_travel(travel_id):
        return [
            t for t in load_json(TICKETS_PATH)
            if t.get("travel_id") == travel_id
        ]

    @staticmethod
    def create(user_id, travel_id, seat_number, status):
        global ticket_id
        tickets = load_json(TICKETS_PATH)

        data = {
            "id": ticket_id,
            "user_id": user_id,
            "travel_id": travel_id,
            "seat_number": seat_number,
            "status": status
        }

        tickets.append(data)
        save_json(TICKETS_PATH, tickets)
        ticket_id += 1
        return data
    
    def reserve(self, user_id, travel_id, seat):
        travels = load_json(TRAVELS_PATH)

        for t in travels:
            if t["id"] == travel_id:
                t["available_seats"].remove(seat)
                if len(t["available_seats"]) == 0:
                    t["status"] = "full"
                break
        save_json(TRAVELS_PATH, travels)

=======
import os
from utils.file_utils import load_json, save_json
from utils.id_counters import ticket_id
from config import TICKETS_PATH, TRAVELS_PATH


class TicketModel:

    @staticmethod
    def load_all():
        return load_json(TICKETS_PATH)

    @staticmethod
    def save_all(data):
        save_json(TICKETS_PATH, data)

    @staticmethod
    def find_reserved_by_user(uid):
        return [
            t for t in load_json(TICKETS_PATH)
            if t.get("user_id") == uid and t.get("status") == "reserved"
        ]

    @staticmethod
    def find_by_id(tid):
        for t in load_json(TICKETS_PATH):
            if t.get("id") == tid:
                return t
        return None

    @staticmethod
    def find_by_travel(travel_id):
        return [
            t for t in load_json(TICKETS_PATH)
            if t.get("travel_id") == travel_id
        ]

    @staticmethod
    def create(user_id, travel_id, seat_number, status):
        global ticket_id
        tickets = load_json(TICKETS_PATH)

        data = {
            "id": ticket_id,
            "user_id": user_id,
            "travel_id": travel_id,
            "seat_number": seat_number,
            "status": status
        }

        tickets.append(data)
        save_json(TICKETS_PATH, tickets)
        ticket_id += 1
        return data
    
    def reserve(self, user_id, travel_id, seat):
        travels = load_json(TRAVELS_PATH)

        for t in travels:
            if t["id"] == travel_id:
                t["available_seats"].remove(seat)
                if len(t["available_seats"]) == 0:
                    t["status"] = "full"
                break
        save_json(TRAVELS_PATH, travels)

>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
        return self.create(user_id, travel_id, seat, "reserved")