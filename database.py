# .\.venv\Scripts\Activate.ps1
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

import psycopg
from getpass import getpass

senha_banco = getpass("Digite a senha do PostgreSQL: ")

conexao = psycopg.connect(
    host="localhost",
    dbname="casa_apostas",
    user="postgres",
    password=senha_banco,
    port=5432
)

print("Conexão realizada com sucesso!")

cursor = conexao.cursor()

login_digitado = input("Digite o login que deseja procurar: ")

cursor.execute(
    "select id, nome, login, saldo from usuario where login = %s;",
    (login_digitado,)
)

usuario = cursor.fetchone()

if usuario:
    print("Usuário encontrado!")
    print("ID:", usuario[0])
    print("Nome:", usuario[1])
    print("Login:", usuario[2])
    print("Saldo:", usuario[3])
else:
    print("Usuário não encontrado!")


cursor.close()

conexao.close()