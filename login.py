from getpass import getpass
import psycopg
from werkzeug.security import check_password_hash


def autenticar(login_digitado, senha_digitada, senha_banco):
    with psycopg.connect(
        host="localhost",
        dbname="casa_apostas",
        user="postgres",
        password=senha_banco,
        port=5432,
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT login, senha_hash FROM usuario WHERE login = %s",
                (login_digitado,),
            )
            usuario = cursor.fetchone()

            print("conta encontrada no banco?", bool is not None)

    if usuario:
        if check_password_hash(usuario[1], senha_digitada):
            return True

    return False


if __name__ == "__main__":
    login_digitado = input("Digite seu login: ")
    senha_digitada = getpass("Digite sua senha: ")
    senha_banco = getpass("Digite a senha do PostgreSQL: ")

    resultado = autenticar(login_digitado, senha_digitada, senha_banco)

    if resultado:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos!")