<<<<<<< HEAD
import os
from utils.file_utils import load_json, save_json
from utils.id_counters import travel_id
from config import TRAVELS_PATH



class TravelModel:

    @staticmethod
    def load_all():
        return load_json(TRAVELS_PATH)

    @staticmethod
    def save_all(data):
        save_json(TRAVELS_PATH, data)

    @staticmethod
    def find(tid):
        for t in load_json(TRAVELS_PATH):
            if t.get("id") == tid:
                return t
        return None

    @staticmethod
    def create(origin, destination, starting_time, duration,
               max_passengers, available_seats, price, status):
        global travel_id
        travels = load_json(TRAVELS_PATH)

        data = {
            "id": travel_id,
            "origin": origin,
            "destination": destination,
            "starting_time": starting_time,
            "duration": duration,
            "max_passengers": max_passengers,
            "available_seats": available_seats,
            "price": price,
            "status": status
        }

        travels.append(data)
        save_json(TRAVELS_PATH, travels)
        travel_id += 1
        return data
    
    def search_available(self, origin):
        return [
            t for t in TravelModel.load_all()
            if t["origin"] == origin and t["status"] == "available"
        ]

=======
import os
from utils.file_utils import load_json, save_json
from utils.id_counters import travel_id
from config import TRAVELS_PATH



class TravelModel:

    @staticmethod
    def load_all():
        return load_json(TRAVELS_PATH)

    @staticmethod
    def save_all(data):
        save_json(TRAVELS_PATH, data)

    @staticmethod
    def find(tid):
        for t in load_json(TRAVELS_PATH):
            if t.get("id") == tid:
                return t
        return None

    @staticmethod
    def create(origin, destination, starting_time, duration,
               max_passengers, available_seats, price, status):
        global travel_id
        travels = load_json(TRAVELS_PATH)

        data = {
            "id": travel_id,
            "origin": origin,
            "destination": destination,
            "starting_time": starting_time,
            "duration": duration,
            "max_passengers": max_passengers,
            "available_seats": available_seats,
            "price": price,
            "status": status
        }

        travels.append(data)
        save_json(TRAVELS_PATH, travels)
        travel_id += 1
        return data
    
    def search_available(self, origin):
        return [
            t for t in TravelModel.load_all()
            if t["origin"] == origin and t["status"] == "available"
        ]

>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
