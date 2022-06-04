from flask import Flask
from random import randint

app = Flask(__name__)

my_number = randint(1, 1001)


@app.route("/")
def guess_the_number():
    while True:
        try:
            user_choice = int(input("Spróbuj zgadnąć liczbę: "))
            if user_choice == my_number:
                return "Gratulacje, udało Ci się!"
            elif user_choice < my_number:
                print("Za mało!")
            elif user_choice > my_number:
                print("Za dużo!")
        except:
            print("Musisz wpisać liczbę!")

app.run(port=6009)
