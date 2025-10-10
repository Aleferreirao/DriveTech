import mysql.connector

#Dados do servidor MySQL
HOST = "localhost"
USER = "root"
PASSWORD = "senac"
DB_NAME = "escola_db" #nome do banco de dados

def conectar(usando_banco=True):
    """Conectar ao Mysql 
    -usando_banco=True -> conectar direto ao schema DB_NAME
    -usando_banco=False -> conectar sem definir um banco"""
    if usando_banco:
        return mysql.connector.connect(
            host = HOST,
            user = USER,
            port = "3306",
            password = PASSWORD,
            database = DB_NAME
        )
    else:
        return mysql.connector.connect(
            host = HOST,
            user = USER,
            port="3306",
            password = PASSWORD
        ) 

def criar_banco():
    #Criar banco caso não exista
    conn = conectar(usando_banco=False) #Cria uma instância de conexão com o banco
    cursor = conn.cursor() # Aponta para o Banco de Dadosa
    cursor.execute(""" CREATE DATABASE 
                   IF NOT EXISTS {DB_NAME}""")
    conn.commit() # salva as alterações no banco
    conn.close() # fecha a conexão com o banco


def criar_tabelas():
    #cria as tabelas (curso, turma, aluno) 
    # se não existirem do BD
    conn = conectar() # abre a conexão com o banco
    cursor = conn.cursor() # cria um cursor que aponta pro BD e executa intruções SQL
    
    # Tabela de clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT,
            cpf TEXT UNIQUE
        )
    """)

    # Tabela de veículos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            marca TEXT,
            modelo TEXT,
            ano INTEGER,
            placa TEXT UNIQUE,
            km_atual INTEGER,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )
    """)

    # Tabela de manutenções
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS manutencoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            veiculo_id INTEGER NOT NULL,
            descricao TEXT NOT NULL,
            data TEXT NOT NULL,
            km_realizada INTEGER,
            km_proxima INTEGER,
            data_proxima TEXT,
            FOREIGN KEY(veiculo_id) REFERENCES veiculos(id)
        )
    """)

    conn.commit()
    conn.close()
