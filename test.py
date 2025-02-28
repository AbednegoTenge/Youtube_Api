import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes': 10, 'name': 'Chris', 'views': 100},
        {'likes': 70, 'name': 'Igi', 'views': 200},
        {'likes': 249000, 'name': 'HOW TO MAKE REST APIs', 'views': 1000000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + 'video/0')
print(response)
input()
response = requests.get(BASE + 'video/2')
print(response.json()) 