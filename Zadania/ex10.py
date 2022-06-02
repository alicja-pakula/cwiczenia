from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def return_text():
    return "Wybrałeś " + request.method

app.run(port=5000)