from api_client import fetch_data
from data_processor import process_and_save

api_url = "https://jsonplaceholder.typicode.com/todos"

users_data = fetch_data(api_url)

output_path = "3/result.csv"
try:
        process_and_save(users_data, output_path)
except TypeError:
        print("Your url is either wrong or you lost internet connection")