import requests
from pymongo import MongoClient
from bson.json_util import dumps


client = MongoClient(port=27017)
db = client.players

# keyValue = []
# for i in range(300):
#     data = requests.get("http://127.0.0.1:5000/get_data/" + str(i)).json()
#     name = str(data['name'] or '') + ' ' +  str(int(data['id'] or 0))
#     db.playerKeys.insert_one({'name': name})
# db.playerKeys.delete_many({'name': 'Stephen Curry115'})
print(dumps(db.playerKeys.find({})))