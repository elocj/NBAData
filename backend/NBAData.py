import os

import requests
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import json
from flask import request
from flask import redirect

app = Flask(__name__, template_folder = "../frontend/templates/", static_folder = "../frontend/static/")
app.config["DEBUG"] = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/get_data', methods = ['GET', 'POST'])
def get_data():
    r = requests.get("https://www.balldontlie.io/api/v1/stats?player_ids[]=115&per_page=25").json()
    arr = []
    date = []
    for data in r['data']:
        arr.append([data['pts'], data['reb'], data['stl'], data['turnover'], data['ast'], data['blk']])
        day = data['game']['date'].split('T')
        date.append(day[0].split('-'))
    arr = calcScore(arr)
    return jsonify({'payload': {'date': date, 'arr': arr}})

def calcScore(arr):
    score = []
    for pts, reb, stl, turnover, ast, blk in arr:
        score.append(pts * 1 + reb * 1.2 + stl * 3 + turnover * -1 + ast * 1.5 + blk * 3)
    return score

app.run()