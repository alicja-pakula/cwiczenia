from flask import Flask

app = Flask(__name__)

my_list = [1, 4, 76, 34, 5]

@app.route("/parametr/<int:x>")
def my_index(x):
    return str(my_list[int(x)])

@app.route("/")
def hello():
    return "Witaj użytkowniku!"


@app.route("/hello/<name>/<nazwisko>")
def hello_user(name, nazwisko):
    return "Hello " + name + " " + nazwisko + "!"


app.run(port=6001)
