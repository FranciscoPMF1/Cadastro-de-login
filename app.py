from flask import request
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem vindo ao FutBet!"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        print("O formulário foi enviado!")

    return render_template("login.html")