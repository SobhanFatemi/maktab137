from utils.file_utils import load_json
from utils.file_utils import ensure_file
from config import USERS_PATH, TRAVELS_PATH, TICKETS_PATH, PAYMENTS_PATH

admin_id = 100100
user_id = 200100
travel_id = 300100
ticket_id = 400100
payment_id = 500100

def load_last_id(path, start_id):
    ensure_file(path, [])
    data = load_json(path)
    if data:
        return max(item["id"] for item in data) + 1
    return start_id

admin_id = load_last_id(USERS_PATH, admin_id)
user_id = load_last_id(USERS_PATH, user_id)
travel_id = load_last_id(TRAVELS_PATH, travel_id)
ticket_id = load_last_id(TICKETS_PATH, ticket_id)
payment_id = load_last_id(PAYMENTS_PATH, payment_id)
