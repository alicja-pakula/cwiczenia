from flask import Flask
from random import randint
from flask import jsonify

app = Flask(__name__)

@app.route("/losuj" , methods =['GET'])
def draw_a_number():
    my_digits = [randint(0,9), randint(0,9), randint(0,9)]
    return jsonify(my_digits)

app.run(port=6010)