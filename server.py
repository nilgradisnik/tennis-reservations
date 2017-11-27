
from flask import Flask
from flask import Response
from flask import json

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
def api_reservations():
    js = json.dumps(RESERVATIONS)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://localhost:5000'

    return resp
