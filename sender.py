import requests


mydata = {
    'scene': 'TestRoom',
    'roomName': 'userId9436923692364936'
}

post_response = requests.post(
    'http://127.0.0.1:5000/add_room',
    json=mydata
)

print(post_response.text)

get_response = requests.get(
    'http://127.0.0.1:5000/get_rooms',
    params={'scene': 'TestRoom'})

print(get_response.text)

get_response = requests.get(
    'http://127.0.0.1:5000/all_rooms')

print(get_response.text)

get_response = requests.post(
    'http://127.0.0.1:5000/remove_room',
    json=mydata)

print(get_response.text)

get_response = requests.get(
    'http://127.0.0.1:5000/all_rooms')

print(get_response.text)
