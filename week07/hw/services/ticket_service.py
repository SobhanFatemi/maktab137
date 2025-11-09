from models.ticket import TicketModel
from models.travel import TravelModel
from models.travel import TRAVELS_PATH
from utils.file_utils import save_json, load_json


class TicketService:

    def reserve(self, user_id, travel_id, seat):
        travels = load_json(TRAVELS_PATH)

        # remove seat
        for t in travels:
            if t["id"] == travel_id:
                t["available_seats"].remove(seat)
                if len(t["available_seats"]) == 0:
                    t["status"] = "full"
                break

        save_json(TRAVELS_PATH, travels)

        return TicketModel.create(user_id, travel_id, seat, "reserved")

    def users_in_travel(self, travel_id):
        return TicketModel.find_by_travel(travel_id)
