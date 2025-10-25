import sqlite3
from database.database import conectar

class Cliente:
    def __init__(self, cpf_cliente, nme_cliente, tel_cliente, email_cliente, end_cliente):
        self.cpf_cliente = cpf_cliente
        self.nme_cliente = nme_cliente
        self.tel_cliente = tel_cliente
        self.email_cliente = email_cliente
        self.end_cliente = end_cliente

    def adicionar(self):
        try:
            con = conectar()
            cur = con.cursor()
            cur.execute(
                "INSERT INTO cliente (cpf_cliente, nme_cliente, tel_cliente, email_cliente, end_cliente) VALUES (?, ?, ?, ?, ?)",
                (self.cpf_cliente, self.nme_cliente, self.tel_cliente, self.email_cliente, self.end_cliente)
            )
            con.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"❌ Erro ao adicionar cliente: {e}")
            return False
        finally:
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
    def buscar_por_cpf(cpf_cliente):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM cliente WHERE cpf_cliente = ?", (cpf_cliente,))
        cliente = cur.fetchone()
        con.close()
        return cliente

class Veiculo:
    def __init__(self, placa_veiculo, marc_veiculo, mode_veiculo, ano_veiculo, km_atual_veiculo, cpf_cliente_veiculo):
        self.placa_veiculo = placa_veiculo
        self.marc_veiculo = marc_veiculo
        self.mode_veiculo = mode_veiculo
        self.ano_veiculo = ano_veiculo
        self.km_atual_veiculo = km_atual_veiculo
        self.cpf_cliente_veiculo = cpf_cliente_veiculo

    def adicionar(self):
        try:
            con = conectar()
            cur = con.cursor()
            cur.execute(
                "INSERT INTO veiculo (placa_veiculo, marc_veiculo, mode_veiculo, ano_veiculo, km_atual_veiculo, cpf_cliente_veiculo) VALUES (?, ?, ?, ?, ?, ?)",
                (self.placa_veiculo, self.marc_veiculo, self.mode_veiculo, self.ano_veiculo, self.km_atual_veiculo, self.cpf_cliente_veiculo)
            )
            con.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"❌ Erro ao adicionar veículo: {e}")
            return False
        finally:
            con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT v.*, c.nme_cliente 
            FROM veiculo v 
            LEFT JOIN cliente c ON v.cpf_cliente_veiculo = c.cpf_cliente
        """)
        dados = cur.fetchall()
        con.close()
        return dados

    @staticmethod
    def buscar_por_cliente(cpf_cliente):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM veiculo WHERE cpf_cliente_veiculo = ?", (cpf_cliente,))
        veiculos = cur.fetchall()
        con.close()
        return veiculos

class Manutencao:
    def __init__(self, veic_manutencao, serv_manutencao, dta_manutencao, pecs_manutencao, placa_veiculo_manutencao):
        self.veic_manutencao = veic_manutencao
        self.serv_manutencao = serv_manutencao
        self.dta_manutencao = dta_manutencao
        self.pecs_manutencao = pecs_manutencao
        self.placa_veiculo_manutencao = placa_veiculo_manutencao

    def adicionar(self):
        try:
            con = conectar()
            cur = con.cursor()
            cur.execute(
                "INSERT INTO manutencao (veic_manutencao, serv_manutencao, dta_manutencao, pecs_manutencao, placa_veiculo_manutencao) VALUES (?, ?, ?, ?, ?)",
                (self.veic_manutencao, self.serv_manutencao, self.dta_manutencao, self.pecs_manutencao, self.placa_veiculo_manutencao)
            )
            con.commit()
            return True
        except Exception as e:
            print(f"❌ Erro ao adicionar manutenção: {e}")
            return False
        finally:
            con.close()

    @staticmethod
    def listar():
        con = conectar()
        cur = con.cursor()
        cur.execute("""
            SELECT m.*, v.marc_veiculo, v.mode_veiculo 
            FROM manutencao m 
            LEFT JOIN veiculo v ON m.placa_veiculo_manutencao = v.placa_veiculo
        """)
        dados = cur.fetchall()
        con.close()
        return dados

    @staticmethod
    def buscar_por_veiculo(placa_veiculo):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM manutencao WHERE placa_veiculo_manutencao = ?", (placa_veiculo,))
        manutencoes = cur.fetchall()
        con.close()
        return manutencoes