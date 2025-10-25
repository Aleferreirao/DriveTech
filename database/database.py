import sqlite3
import os

DB_NAME = "DriveTech.db"
DB_PATH = os.path.join(os.path.dirname(__file__), '..', DB_NAME)

def conectar():
    """Conecta ao banco de dados SQLite"""
    return sqlite3.connect(DB_PATH)

def criar_tabelas():
    """Cria todas as tabelas necessárias no banco de dados"""
    con = conectar()
    cur = con.cursor()

    # Tabela CLIENTE
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS cliente(
            cpf_cliente VARCHAR(15) PRIMARY KEY NOT NULL,
            nme_cliente VARCHAR(100) NOT NULL,
            tel_cliente VARCHAR(15) NOT NULL,
            email_cliente VARCHAR(50) NOT NULL,
            end_cliente VARCHAR(100) NOT NULL
        )
    """)

    # Tabela VEICULO
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS veiculo(
            id_veiculo INTEGER PRIMARY KEY AUTOINCREMENT,
            placa_veiculo VARCHAR(10) NOT NULL UNIQUE,
            marc_veiculo VARCHAR(30) NOT NULL,
            mode_veiculo VARCHAR(100) NOT NULL,
            ano_veiculo INTEGER NOT NULL,
            km_atual_veiculo INTEGER NOT NULL,
            cpf_cliente_veiculo VARCHAR(15),
            FOREIGN KEY(cpf_cliente_veiculo) REFERENCES cliente(cpf_cliente)
        )
    """)

    # Tabela MANUTENCAO
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS manutencao(
            id_manutencao INTEGER PRIMARY KEY AUTOINCREMENT,
            veic_manutencao VARCHAR(30) NOT NULL,
            serv_manutencao VARCHAR(100) NOT NULL,
            dta_manutencao DATE NOT NULL,
            pecs_manutencao VARCHAR(200),
            placa_veiculo_manutencao VARCHAR(10),
            FOREIGN KEY(placa_veiculo_manutencao) REFERENCES veiculo(placa_veiculo)
        )
    """)

    # Tabela USUARIOS
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(50) UNIQUE NOT NULL,
            senha VARCHAR(50) NOT NULL,
            nivel VARCHAR(20) DEFAULT 'usuario'
        )
    """)

    con.commit()
    con.close()
    print("✅ Tabelas criadas com sucesso!")

# Criar tabelas automaticamente
if __name__ == "__main__":
    criar_tabelas()