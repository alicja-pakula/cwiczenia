from flask import Flask, request

app = Flask(__name__)


@app.route("/form")
def get_from_form():
    return """
        <form action="/wynik" method='POST'>
            <label>
                Liczba 1:
                <input type="text" name="l1">
            </label>
            <label>
                Liczba 2:
                <input type="text" name="l2">
            </label>
            <label>
                <select name="operacja">
                    <option value="dodawanie"> + </option>
                    <option value="odejmowanie"> - </option>
                    <option value="mnożenie"> * </option>
                    <option value="dzielenie"> / </option>
                </select>
            <label>
            <button type="submit">
                Wyślij
            </button>
            </label>
    </form>"""


@app.route("/wynik", methods=['POST'])
def wynik():
    try:
        l1 = int(request.form["l1"])
        l2 = int(request.form["l2"])
    except:
        return "Możesz wpisać tylko liczby!"
    operacja = request.form["operacja"]
    if operacja == "dodawanie":
        return str(l1 + l2)
    elif operacja == "odejmowanie":
        return str(l1 - l2)
    elif operacja == "mnożenie":
        return str(l1 * l2)
    elif operacja == "dzielenie":
        try:
            return str(l1 / l2)
        except ZeroDivisionError:
            return "Nie wolno dzielić przez 0!"


app.run(port=5202)
