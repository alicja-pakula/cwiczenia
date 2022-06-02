from flask import Flask, jsonify
from random import shuffle

app = Flask(__name__)


@app.route("/lotek", methods=['GET'])
def lotek():
    my_list = [a for a in range(1, 50)]
    shuffle(my_list)
    return jsonify(my_list[:5])

app.run(port=5010)
