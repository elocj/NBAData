from flask import Flask
from flask import render_template
from pymongo import MongoClient
from flask import json
from bson.json_util import dumps
import json
from flask import request
from flask import redirect
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient(port=27017)
db = client.players

app = Flask(__name__, template_folder = "../frontend/templates/", static_folder = "../frontend/static/")
app.config["DEBUG"] = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/get_data', methods = ['GET', 'POST'])
def get_data():
    return dumps(db.games.find_one({'id': 115}))

@app.route('/write_players', methods = ['GET', 'POST'])
def write_players():
    if request.form:
        id = 0
        try:
            id += request.form.get('id')
            db.users.insert_one({'userID': id})
        except Exception as e:
            print(e)
    return redirect('/')

app.run()

# Implement MongoDB to read in JSON
# Make it so I can pick any of the players