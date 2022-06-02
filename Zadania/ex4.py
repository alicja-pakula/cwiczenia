from flask import Flask

app = Flask(__name__)


@app.route("/licz/<int:liczba1>/<int:liczba2>", methods=['GET'])
def licz(liczba1, liczba2):
    my_sum = liczba1 + liczba2
    return str(my_sum)


app.run(port=6009)

# GET /licz/liczba1/liczba2
