import requests

def fetch_data(api_url):
    try:
        user_list = requests.get(api_url).json()
        return user_list
    except requests.exceptions.ConnectionError:
        return None