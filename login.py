import psycopg
from getpass import getpass

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
        print("Usuário encontrado!")

    else:
        print("Usuário não encontrado!")
