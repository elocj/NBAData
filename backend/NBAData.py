import os
from random import randint
import requests
from flask import Flask
from flask import render_template
from flask import jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
from flask import json
from bson.json_util import dumps
from bson.json_util import loads
from flask import request
from flask import redirect
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient(port=27017)
# db=client.business
# names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
# company_type = ['LLC','Inc','Company','Corporation']
# company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
# for x in range(1, 501):
#     business = {
#         'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
#         'rating' : randint(1, 5),
#         'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
#     }
#     #Step 3: Insert business object directly into MongoDB via isnert_one
#     result=db.reviews.insert_one(business)
#     #Step 4: Print to the console the ObjectID of the new document
#     print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
# #Step 5: Tell us that you are done
# print('finished creating 500 business reviews')

# fivestar = db.reviews.find_one({'rating': 5})
# print(fivestar)

db = client.players

app = Flask(__name__, template_folder = "../frontend/templates/", static_folder = "../frontend/static/")
app.config["DEBUG"] = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    date = datetime.now() - timedelta(days=265)
    date = date.strftime("%Y-%m-%d")
    # print(date)
    # r = requests.get("https://www.balldontlie.io/api/v1/stats?player_ids[]=237&per_page=10").json()
    # db.games.insert_one(r)
    # db.games.delete_many({})
    # fivestar = db.games.find({})
    # print(db.games.find_one({}))
    # dat = []
    # for doc in fivestar:
    #     dat.append(doc)
    return render_template("index.html")

# @app.route('/get_data/<id>', methods = ['GET', 'POST'])
# def get_data(id):
#     db.games.delete_many({})
#     date = datetime.now() - timedelta(days=265)
#     date = date.strftime("%Y-%m-%d")
#     # print(date)
#     # id = id
#     r = requests.get("https://www.balldontlie.io/api/v1/stats?player_ids[]=" + str(id) + "&per_page=10").json()
#     print(r)
#     arr = []
#     date = []
#     for data in r['data']:
#         arr.append([data['pts'], data['reb'], data['stl'], data['turnover'], data['ast'], data['blk']])
#         day = data['game']['date'].split('T')
#         date.append(day[0].split('-'))
#     arr = calcScore(arr)
#     db.games.insert_one({'id': id, 'date': date, 'arr': arr})
#     # return jsonify({'payload': {'id': id, 'date': date, 'arr': arr}})
#     # db.games.delete_many({})
#     return JSONEncoder().encode(db.games.find_one({'id': id}))

@app.route('/get_data', methods = ['GET', 'POST'])
def get_data():
    db.games.delete_many({})
    for i in range(2):
        db.games.delete_many({})
        date = datetime.now() - timedelta(days=265)
        date = date.strftime("%Y-%m-%d")
        r = requests.get("https://www.balldontlie.io/api/v1/stats?player_ids[]=" + str(i) + "&per_page=10").json()
        print(r)
        arr = []
        date = []
        for data in r['data']:
            arr.append([data['pts'], data['reb'], data['stl'], data['turnover'], data['ast'], data['blk']])
            day = data['game']['date'].split('T')
            date.append(day[0].split('-'))
        arr = calcScore(arr)
        db.games.insert_one({'id': i, 'date': date, 'arr': arr})
    # return jsonify({'payload': {'id': id, 'date': date, 'arr': arr}})
    return dumps(db.games.find_one({'id': 1}))
    # return JSONEncoder().encode({'payload': db.games.find_one({'id': 1})})

def calcScore(arr):
    score = []
    for pts, reb, stl, turnover, ast, blk in arr:
        print(pts, reb, stl, turnover, ast, blk)
        score.append(int(pts or 0) * 1 + int(reb or 0) * 1.2 + int(stl or 0) * 3 + int(turnover or 0) * -1 + int(ast or 0) * 1.5 + int(blk or 0) * 3)
    return score

app.run()

# Implement MongoDB to read in JSON
# Make it so I can pick any of the players