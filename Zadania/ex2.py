from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def get_time():
    return str(datetime.datetime.now())

app.run(port=6005)