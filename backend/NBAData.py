import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__, template_folder = "../frontend/templates/", static_folder = "../frontend/static/")
app.config["DEBUG"] = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    num = None
    if request.form:
        num = request.form.get("num")
        num = turnToArray(num)
    return render_template("index.html", num = num)

def turnToArray(num):
    arr = num.split(',')
    try:
        return [int(value) for value in arr]
    except Exception as e:
        print("Cannot typecast non-numbers")
        print(e)

app.run()