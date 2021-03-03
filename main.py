import json
from os import O_APPEND
from flask import Flask, request, abort

app = Flask(__name__)

with open('rooms.json') as rooms_file:
    db = json.load(rooms_file)


@app.route('/')
def hello():
    return f'Hello, user!'


@app.route('/add_room', methods=['POST'])
def add_room():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'scene' not in data or 'roomName' not in data:
        return abort(400)

    scene = data['scene']
    roomName = data['roomName']

    if not isinstance(scene, str) or not isinstance(roomName, str) or scene == '' or roomName == '':
        return abort(400)

    if scene not in db:
        db[scene] = []

    if roomName in db[scene]:
        return abort(400)

    db[scene].append(roomName)
    return {'Ok': 200}


@app.route('/remove_room', methods=['POST'])
def remove_room():
    data = request.json
    if not isinstance(data, dict):
        return abort(400)

    if 'scene' not in data or 'roomName' not in data:
        return abort(400)

    scene = data['scene']
    roomName = data['roomName']

    if not isinstance(scene, str) or not isinstance(roomName, str) or scene == '' or roomName == '':
        return abort(400)

    if scene not in db or roomName not in db[scene]:
        return abort(400)

    db[scene].remove(roomName)
    return {'Ok': 200}


@app.route('/get_rooms', methods=['GET'])
def get_rooms():
    try:
        scene = request.args['scene']
    except:
        return abort(400)

    if scene not in db:
        return abort(400)

    result = db[scene]
    return {scene: result}


@app.route('/all_rooms', methods=['GET'])
def all_rooms():
    return db


if __name__ == '__main__':
    app.run()
