from models.travel import TravelModel


class TravelService:

    def search_available(self, origin):
        return [
            t for t in TravelModel.load_all()
            if t["origin"] == origin and t["status"] == "available"
        ]

    def find(self, travel_id):
        return TravelModel.find_by_id(travel_id)

    def save(self):
        all_travels = TravelModel.load_all()
        TravelModel.save_all(all_travels)

    def create(self, **kwargs):
        return TravelModel.create(**kwargs)
