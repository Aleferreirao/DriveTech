import sqlite3

DB_NAME = "DriveTech.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabelas():
    con = conectar()
    cur = con.cursor()


    
    cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS cliente(
                        nme_cliente VARCHAR(100) NOT NULL,
                        cpf_cliente VARCHAR(15) PRIMARY KEY NOT NULL,
                        tel_cliente VARCHAR(15) NOT NULL,
                        email_cliente VARCHAR(50) NOT NULL,
                        end_cliente VARCHAR(50) NOT NULL
                    )
                 """)

    cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS veiculo(
                        id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
                        marc_veiculo VARCHAR(30) NOT NULL,
                        mode_veiculo VARCHAR (100) NOT NULL,
                        ano_veiculo DATE NOT NULL,
                        placa_veiculo VARCHAR(30) NOT NULL,
                        km_atual_veiculo INT NOT NULL,
                        cpf_cliente_veiculo VARCHAR, FOREIGN KEY(cpf_cliente_veiculo) REFERENCES cliente(cpf_cliente)
                    )
                 """)
    
    cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS manutencao(
                        id_manutencao INT PRIMARY KEY AUTO_INCREMENT,
                        veic_manutencao VARCHAR(30) NOT NULL,
                        serv_manutencao VARCHAR (100) NOT NULL,
                        dta_manuntencao DATE NOT NULL,
                        pecs_manutencao VARCHAR(30)
                    )
                 """)
    
    cur.execute(""" 
                    CREATE TABLE IF NOT EXISTS relatorio(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(100) NOT NULL,
                        turma_id INT,
                        FOREIGN KEY(turma_id) REFERENCES turmas(id)
                    )
                 """)
    
    #adicionar outras tabelas pendentes ainda acima, e configurar as que ja estão descritas


    con.commit() #salva(confirmar) as alterações no banco
    con.close() #fechar a conexão com o banco
