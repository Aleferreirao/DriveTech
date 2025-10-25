import tkinter as tk
from tkinter import ttk, messagebox
from models.models import Cliente, Veiculo, Manutencao

class ConsultaFrame(tk.Frame):
    def __init__(self, parent, tipo_consulta):
        super().__init__(parent, bg="#F5F5F5")
        self.tipo_consulta = tipo_consulta
        self.criar_interface()

    def criar_interface(self):
        # Dicionário de títulos por tipo
        titulos = {
            "clientes": "Consulta de Clientes",
            "veiculos": "Consulta de Veículos",
            "manutencoes": "Consulta de Manutenções"
        }

        # Título
        titulo = tk.Label(
            self,
            text=titulos.get(self.tipo_consulta, "Consulta"),
            font=("Arial Black", 18),
            bg="#F5F5F5"
        )
        titulo.pack(pady=10)

        # Frame da tabela
        table_frame = tk.Frame(self, bg="#F5F5F5")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Criar tabela conforme o tipo
        if self.tipo_consulta == "clientes":
            self.criar_tabela_clientes(table_frame)
        elif self.tipo_consulta == "veiculos":
            self.criar_tabela_veiculos(table_frame)
        elif self.tipo_consulta == "manutencoes":
            self.criar_tabela_manutencoes(table_frame)

        # Frame dos botões (lado a lado)
        botoes_frame = tk.Frame(self, bg="#F5F5F5")
        botoes_frame.pack(pady=10)

        # Botão Atualizar
        btn_atualizar = tk.Button(
            botoes_frame,
            text="Atualizar Dados",
            command=self.carregar_dados,
            bg="#1976D2",
            fg="white",
            font=("Arial", 10)
        )
        btn_atualizar.pack(side="left", padx=10)

        # Botão Deletar
        btn_deletar = tk.Button(
            botoes_frame,
            text="Deletar Dados",
            command=self.deletar_dados,
            bg="#D32F2F",
            fg="white",
            font=("Arial", 10)
        )
        btn_deletar.pack(side="left", padx=10)

        # Carregar os dados iniciais
        self.carregar_dados()

    # ==== TABELAS ====
    def criar_tabela_clientes(self, parent):
        columns = ("CPF", "Nome", "Telefone", "Email", "Endereço")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True)

    def criar_tabela_veiculos(self, parent):
        columns = ("Placa", "Marca", "Modelo", "Ano", "KM Atual", "Cliente")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(fill="both", expand=True)

    def criar_tabela_manutencoes(self, parent):
        columns = ("Veículo", "Serviço", "Data", "Peças", "Placa")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=130)
        self.tree.pack(fill="both", expand=True)

    # ==== CARREGAR DADOS ====
    def carregar_dados(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        if self.tipo_consulta == "clientes":
            dados = Cliente.listar()
            for c in dados:
                self.tree.insert("", "end", values=c)

        elif self.tipo_consulta == "veiculos":
            dados = Veiculo.listar()
            for v in dados:
                self.tree.insert("", "end", values=(
                    v[0], v[1], v[2], v[3], v[4], v[6]
                ))

        elif self.tipo_consulta == "manutencoes":
            dados = Manutencao.listar()
            for m in dados:
                self.tree.insert("", "end", values=(
                    m[1], m[2], m[3], m[4], m[5]
                ))

    # ==== DELETAR DADOS ====
    def deletar_dados(self):
        item_selecionado = self.tree.focus()
        if not item_selecionado:
            messagebox.showwarning("Atenção", "Selecione um registro para deletar.")
            return

        valores = self.tree.item(item_selecionado, "values")
        if not valores:
            return

        confirm = messagebox.askyesno("Confirmar", "Deseja realmente deletar este registro?")
        if not confirm:
            return

        try:
            con = None
            from database.database import conectar
            con = conectar()
            cur = con.cursor()

            if self.tipo_consulta == "clientes":
                cpf = valores[0]
                cur.execute("DELETE FROM cliente WHERE cpf_cliente = ?", (cpf,))
            elif self.tipo_consulta == "veiculos":
                placa = valores[0]
                cur.execute("DELETE FROM veiculo WHERE placa_veiculo = ?", (placa,))
            elif self.tipo_consulta == "manutencoes":
                placa = valores[4]
                cur.execute("DELETE FROM manutencao WHERE placa_veiculo_manutencao = ?", (placa,))

            con.commit()
            self.tree.delete(item_selecionado)
            messagebox.showinfo("Sucesso", "Registro deletado com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao deletar: {e}")
        finally:
            if con:
                con.close()
