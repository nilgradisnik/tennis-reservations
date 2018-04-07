
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
        playtime = request.args.get('hour')
        js = json.dumps(RESERVATIONS[playtime])
        resp = Response(js, status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://localhost:5000'
        return resp

    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'text/plain':
            return "Text Message: " + request.data

        elif request.headers['Content-Type'] == 'application/json':
            return "JSON Message: " + json.dumps(request.json)

        elif request.headers['Content-Type'] == 'application/octet-stream':
            f = open('./binary', 'wb')
            f.write(request.data)
            f.close()
            return "Binary message written!"

        else:
            return "415 Unsupported Media Type ;)"
