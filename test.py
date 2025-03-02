import requests

BASE = "http://127.0.0.1:5000/"

def patch(video_id, data):
    if not isinstance(data, dict):
        raise TypeError('Input must be a dictionary')
    response = requests.patch(BASE + f'video/{video_id}', data)
    print(response.json())

def get(video_id):
    response = requests.get(BASE + f'video/{video_id}')
    print(response.json())

def post(data):
    if not isinstance(data, dict):
        raise TypeError('Input must be a dictionary')
    response = requests.post(BASE + f'video', data)
    print(response.json())

def put(video_id, data):
    if not isinstance(data, dict):
        raise TypeError('Input must be a dictonary')
    response = requests.put(BASE + f'video/{video_id}', data)
    print(response.json())

def delete(video_id):
    response = requests.delete(BASE + f'video/{video_id}')
    if response.status_code == 204:
        print(f'Video with id {video_id} deleted')
    else:
        print(response.text)


# patch(2, {'likes': 10, 'name': 'Tim', 'views': 1000})
# get(4)
# post({'likes': 200, 'name': 'Kingdom of Apes','views': 1000})
# delete(3)

