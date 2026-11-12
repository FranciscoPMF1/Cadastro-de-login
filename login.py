import psycopg
from getpass import getpass
from werkzeug.security import check_password_hash

login_digitado = input("Digite seu login: ")
senha_digitada = getpass("Digite sua senha: ")

senha_banco = getpass("Digite a senha do Postgres: ")


with psycopg.connect(
    host = "localhost",
    dbname = "casa_apostas",
    user = "postgres",
    password = senha_banco,
    port = 5432
) as conexao:

    print("Conexão realizada com sucesso!")

    cursor = conexao.cursor()

    cursor.execute(
        "select login, senha_hash from usuario where login = %s",
        (login_digitado,)
    )

    usuario = cursor.fetchone()

    if usuario:

        if check_password_hash(usuario[1], senha_digitada):
            print("Login realizado com sucesso!")   

        else:
            print("Usuário ou senha inncorretos!")
    else:
            print("Usuário ou senha inncorretos!")
