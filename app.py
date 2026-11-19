import os
from flask import Flask, render_template, request
from login import autenticar
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo ao FutBet!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_digitado = request.form.get("login", "").strip()
        senha_digitada = request.form.get("senha", "")

        if not login_digitado or not senha_digitada:
            return "Preencha o login e a senha."

        senha_banco = os.environ["FUTBET_DB_PASSWORD"]

        if autenticar(login_digitado, senha_digitada, senha_banco):
            return "Login realizado com sucesso!"

        return "Usuário ou senha incorretos!"

    return render_template("login.html")