from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def get_date():
        return str(datetime.date.today())


app.run(port=6001)
