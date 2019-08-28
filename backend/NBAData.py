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

@app.route('/get_data/<val>', methods = ['GET', 'POST'])
def get_data(val):
    return dumps(db.games.find_one({'id': int(val)}))

@app.route('/get_users', methods = ['GET', 'POST'])
def get_users():
    users = db.users.find({})
    id = []
    for user in users:
        id.append(user)
    return dumps(id)

@app.route('/delete_player', methods = ['GET', 'POST'])
def delete_player():
    if request.form:
        try:
            id = int(request.form.get('id'))
            db.users.delete_many({'userID': id})
        except Exception as e:
            print(e)
    return redirect('/')

@app.route('/write_player', methods = ['GET', 'POST'])
def write_player():
    if request.form:
        try:
            id = int(request.form.get('id'))
            db.users.insert_one({'userID': id})
        except Exception as e:
            print(e)
    return redirect('/')

app.run()

# Now what i want to do is get a list of all/most players and their corresponding keys and then autofill suggest