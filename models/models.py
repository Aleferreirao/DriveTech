# models.py
import sqlite3
from database.database import conectar
# Classe base: Cliente
class Pessoa:
    def __init__(self, nome, cpf=None, telefone=None, email=None, endereço=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereço = endereço


# Subclasse: Cliente
class Cliente(Pessoa):
    def __init__(self, nome, telefone=None, email=None, cpf=None):
        super().__init__(nome, telefone, email, cpf)

    def adicionar(self):
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO cliente (nome,cpf, telefone, email, endereço) VALUES (?, ?, ?, ?, ?)",
            (self.nome,self.cpf, self.telefone, self.email, self.endereço)
        )
        con.commit()
        con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM cliente")
        dados = cur.fetchall()
        con.close()
        return dados

    @staticmethod
    def atualizar(cpf_cliente, nome=None, telefone=None, email=None, endereço=None):
        con = conectar()
        cur = con.cursor()
        if nome:
            cur.execute("UPDATE cliente SET nome=? WHERE id=?", (nome, cpf_cliente))
        if telefone:
            cur.execute("UPDATE cliente SET telefone=? WHERE id=?", (telefone, cpf_cliente))
        if email:
            cur.execute("UPDATE cliente SET email=? WHERE id=?", (email, cpf_cliente))
        if endereço:
            cur.execute("UPDATE cliente SET endereço=? WHERE id=?", (endereço, cpf_cliente))
        con.commit()
        con.close()

    @staticmethod
    def deletar(cpf_cliente):
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM cliente WHERE id=?", (cpf_cliente,))
        con.commit()
        con.close()

# Classe: Veiculo
class Veiculo:
    def __init__(self, cpf_cliente, marca, modelo, ano, placa, km_atual=0):
        self.cpf_cliente = cpf_cliente
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.km_atual = km_atual

    def adicionar(self):
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO veiculo (cpf_cliente, marca, modelo, ano, placa, km_atual) VALUES (?, ?, ?, ?, ?, ?)",
            (self.cpf_cliente, self.marca, self.modelo, self.ano, self.placa, self.km_atual)
        )
        con.commit()
        con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM veiculo")
        dados = cur.fetchall()
        con.close()
        return dados

# Classe: Manutencao
class Manutencao:
    def __init__(self, cpf_cliente, descricao, data, km_realizada, km_proxima=None, data_proxima=None):
        self.cpf_cliente = cpf_cliente
        self.descricao = descricao
        self.data = data
        self.km_realizada = km_realizada
        self.km_proxima = km_proxima
        self.data_proxima = data_proxima

    def adicionar(self):
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO manutencoes (veiculo_id, descricao, data, km_realizada, km_proxima, data_proxima) VALUES (?, ?, ?, ?, ?, ?)",
            (self.cpf_cliente, self.descricao, self.data, self.km_realizada, self.km_proxima, self.data_proxima)
        )
        con.commit()
        con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM manutencoes")
        dados = cur.fetchall()
        con.close()
        return dados


# Classes de Usuário e Admin
class Usuario:
    def __init__(self, nome, email, senha, nivel="usuario"):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.nivel = nivel

    def adicionar(self):
        con = conectar()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO usuarios (nome, email, senha, nivel) VALUES (?, ?, ?, ?)",
            (self.nome, self.email, self.senha, self.nivel)
        )
        con.commit()
        con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT id, nome, email, nivel FROM usuarios")
        dados = cur.fetchall()
        con.close()
        return dados

class Administrador(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha, nivel="admin")