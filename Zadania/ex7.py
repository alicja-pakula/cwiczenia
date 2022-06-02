from flask import Flask, request

app = Flask(__name__)


@app.route("/form")
def get_from_form():
    return """
        <form action="/hello" method='POST'>
            <label>
                Imię:
                <input type="text" name="user_name">
            </label>
            <label>
            <button type="submit">
                Wyślij
            </button>
            </label>
    </form>"""


@app.route("/hello", methods=['POST'])
def hello_user():
    user_name = request.form["user_name"]
    return "Witaj " + user_name + "!"


app.run(port=6520)
