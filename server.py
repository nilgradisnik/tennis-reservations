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

@app.route('/reservations', methods = ['GET', 'POST'])
def api_reservations():
    if request.method == 'GET':
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
    elif request.method == 'POST':
        if request.args.get('hour') in RESERVATIONS.keys():
            payload = request.get_json()
            RESERVATIONS[payload['hour']] = {'available': False, 'player': payload['player']}
            js = json.dumps(payload)
            resp = Response(js, status=201, mimetype='application/json')
            return resp
        else:
            resp = Response(response='Invalid body', status=400, mimetype='application/json' )
            return resp
    else:
        return "Unsupported media type ;)"
