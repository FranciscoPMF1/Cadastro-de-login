import psycopg
from getpass import getpass
from werkzeug.security import generate_password_hash

#informações do novo usuário
nome = input("Digite seu nome: ").strip()
login = input("Digite seu login: ").strip()
senha = getpass("Digite sua senha: ")

if not nome or not login or not senha:
    print("Preencha todos os campos!")
else:
    #transformamos a senha em um hash seguro
    senha_hash = generate_password_hash(senha)

    #conexão com postgre
    senha_banco = getpass("Senha do PostegreSQL: ")

    with psycopg.connect(
        host = "localhost",
        dbname = "casa_apostas",
        user = "postgres",
        password = senha_banco,
        port = 5432
    ) as conexao:

        with conexao.cursor() as cursor:
            cursor.execute(
                  """
                INSERT INTO usuario (nome, login, senha_hash)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (nome, login, senha_hash)
            )

            novo_id = cursor.fetchone()[0]

    print("Cadastro realizado com sucesso!")
    print("ID do novo usuário:", novo_id)