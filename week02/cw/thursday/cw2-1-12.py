import requests

url = "https://api.github.com"

response = list(requests.get(url))

print(response)