import requests

BASE = "http://127.0.0.1:5000/"

update = requests.get(BASE + 'video/2')
print(update.json())
