import requests
from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient(port=27017)
db = client.players

def calcScore(arr):
    score = []
    for pts, reb, stl, turnover, ast, blk in arr:
        print(pts, reb, stl, turnover, ast, blk)
        score.append(int(pts or 0) * 1 + int(reb or 0) * 1.2 + int(stl or 0) * 3 + int(turnover or 0) * -1 + int(ast or 0) * 1.5 + int(blk or 0) * 3)
    return score

db.games.delete_many({})
for i in range(100, 150):
    print(i)
    dateCurr = datetime.now() - timedelta(days=300)
    dateCurr = dateCurr.strftime("%Y")
    payload = {'player_ids[]': i, 'per_page': 100, 'seasons[]': 2018}
    r = requests.get("https://www.balldontlie.io/api/v1/stats", params=payload).json()
    print(r)
    arr = []
    date = []
    name = None
    for data in r['data']:
        arr.append([data['pts'], data['reb'], data['stl'], data['turnover'], data['ast'], data['blk']])
        day = data['game']['date'].split('T')
        date.append(day[0].split('-'))
        name = data['player']['first_name'] + " " + data['player']['last_name']
    arr = calcScore(arr)
    db.games.insert_one({'id': i, 'date': date, 'arr': arr, 'name': name})