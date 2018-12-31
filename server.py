from flask import Flask
from flask import Response
from flask import json
from flask import request

app = Flask(__name__)

RESERVATIONS = {}
for hour in ["10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm", "10pm"]:
    RESERVATIONS[hour] = {
    "available": True,
    "player": None
}

@app.route("/")
def index():
    return "Welcome to tennis reservations"

@app.route('/reservations', methods = ['GET'])
def reservations_get():
    if request.args.get('hour') not in RESERVATIONS.keys() and request.args.get('hour') is not None:
        resp = Response(response='Invalid hour format', status=400)
        return resp
    elif request.args.get('hour') in RESERVATIONS.keys():
        playtime = request.args.get('hour')
        js = json.dumps(RESERVATIONS[playtime])
        resp = Response(js, status=200, mimetype='application/json')
        return resp
    elif request.args.get('hour') is None:
        js = json.dumps(RESERVATIONS)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/reservations', methods = ['POST'])
def reservations_post():
    payload = request.get_json()
    print(payload['hour'])
    if not request.is_json:
        resp = Response(status = 400, response='Invalid body')
        return resp
    elif payload['hour'] is False:
        resp = Response(status = 400, response='Invalid hour')
        return resp
    elif payload['hour'] in RESERVATIONS.keys():
        RESERVATIONS[payload['hour']] = {'available': False, 'player': payload['player']}
        js = json.dumps(payload)
        resp = Response(js, status=201, mimetype='application/json')
        return resp
    else:
        resp = Response(response='Unsupported media type', status=400, mimetype='application/json' )
        return resp
