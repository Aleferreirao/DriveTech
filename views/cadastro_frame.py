import tkinter as tk
from tkinter import messagebox
from models.models import Cliente, Veiculo

class CadastroFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5F5F5")
        self.criar_interface()

    def criar_interface(self):
        # Título
        titulo = tk.Label(self, text="Cadastro de Cliente e Veículo", font=("Arial Black", 18), bg="#F5F5F5")
        titulo.pack(pady=10)

        form_frame = tk.Frame(self, bg="#F5F5F5")
        form_frame.pack(pady=10)

        # ----------- DADOS DO CLIENTE -----------
        cliente_frame = tk.LabelFrame(form_frame, text="Dados do Cliente", padx=10, pady=10, bg="white", font=("Arial", 10, "bold"))
        cliente_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        tk.Label(cliente_frame, text="Nome completo:", bg="white", font=("Arial", 9)).grid(row=0, column=0, sticky="e", pady=5)
        self.entry_nome = tk.Entry(cliente_frame, width=30, font=("Arial", 9))
        self.entry_nome.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(cliente_frame, text="CPF:", bg="white", font=("Arial", 9)).grid(row=1, column=0, sticky="e", pady=5)
        self.entry_cpf = tk.Entry(cliente_frame, width=30, font=("Arial", 9))
        self.entry_cpf.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(cliente_frame, text="Telefone:", bg="white", font=("Arial", 9)).grid(row=2, column=0, sticky="e", pady=5)
        self.entry_telefone = tk.Entry(cliente_frame, width=30, font=("Arial", 9))
        self.entry_telefone.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(cliente_frame, text="Email:", bg="white", font=("Arial", 9)).grid(row=3, column=0, sticky="e", pady=5)
        self.entry_email = tk.Entry(cliente_frame, width=30, font=("Arial", 9))
        self.entry_email.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(cliente_frame, text="Endereço:", bg="white", font=("Arial", 9)).grid(row=4, column=0, sticky="e", pady=5)
        self.entry_endereco = tk.Entry(cliente_frame, width=30, font=("Arial", 9))
        self.entry_endereco.grid(row=4, column=1, pady=5, padx=5)

        # ----------- DADOS DO VEÍCULO -----------
        veiculo_frame = tk.LabelFrame(form_frame, text="Dados do Veículo", padx=10, pady=10, bg="white", font=("Arial", 10, "bold"))
        veiculo_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        tk.Label(veiculo_frame, text="Marca:", bg="white", font=("Arial", 9)).grid(row=0, column=0, sticky="e", pady=5)
        self.entry_marca = tk.Entry(veiculo_frame, width=30, font=("Arial", 9))
        self.entry_marca.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(veiculo_frame, text="Modelo:", bg="white", font=("Arial", 9)).grid(row=1, column=0, sticky="e", pady=5)
        self.entry_modelo = tk.Entry(veiculo_frame, width=30, font=("Arial", 9))
        self.entry_modelo.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(veiculo_frame, text="Placa:", bg="white", font=("Arial", 9)).grid(row=2, column=0, sticky="e", pady=5)
        self.entry_placa = tk.Entry(veiculo_frame, width=30, font=("Arial", 9))
        self.entry_placa.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(veiculo_frame, text="Ano:", bg="white", font=("Arial", 9)).grid(row=3, column=0, sticky="e", pady=5)
        self.entry_ano = tk.Entry(veiculo_frame, width=30, font=("Arial", 9))
        self.entry_ano.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(veiculo_frame, text="KM Atual:", bg="white", font=("Arial", 9)).grid(row=4, column=0, sticky="e", pady=5)
        self.entry_km = tk.Entry(veiculo_frame, width=30, font=("Arial", 9))
        self.entry_km.grid(row=4, column=1, pady=5, padx=5)
        self.entry_km.insert(0, "0")

        # Botões
        btn_frame = tk.Frame(self, bg="#F5F5F5")
        btn_frame.pack(pady=20)

        btn_cadastrar = tk.Button(btn_frame, text="Cadastrar", command=self.salvar_dados,
                                  bg="#2E7D32", fg="white", width=15, height=2, font=("Arial", 10, "bold"))
        btn_cadastrar.grid(row=0, column=0, padx=10)

        btn_limpar = tk.Button(btn_frame, text="Limpar Campos", command=self.limpar_campos,
                               bg="#D32F2F", fg="white", width=15, height=2, font=("Arial", 10))
        btn_limpar.grid(row=0, column=1, padx=10)

    def salvar_dados(self):
        # Dados do cliente
        nme_cliente = self.entry_nome.get().strip()
        cpf_cliente = self.entry_cpf.get().strip()
        tel_cliente = self.entry_telefone.get().strip()
        email_cliente = self.entry_email.get().strip()
        end_cliente = self.entry_endereco.get().strip()

        # Dados do veículo
        marc_veiculo = self.entry_marca.get().strip()
        mode_veiculo = self.entry_modelo.get().strip()
        placa_veiculo = self.entry_placa.get().strip().upper()
        ano_veiculo = self.entry_ano.get().strip()
        km_atual_veiculo = self.entry_km.get().strip() or "0"

        # Validações
        if not nme_cliente or not cpf_cliente or not placa_veiculo:
            messagebox.showerror("Erro", "❌ Nome, CPF e Placa são obrigatórios!")
            return

        if not ano_veiculo.isdigit():
            messagebox.showerror("Erro", "❌ Ano deve ser um número!")
            return

        if not km_atual_veiculo.isdigit():
            messagebox.showerror("Erro", "❌ KM deve ser um número!")
            return

        try:
            # Cadastrar cliente
            cliente = Cliente(cpf_cliente, nme_cliente, tel_cliente, email_cliente, end_cliente)
            if cliente.adicionar():
                # Cadastrar veículo
                veiculo = Veiculo(placa_veiculo, marc_veiculo, mode_veiculo, int(ano_veiculo), int(km_atual_veiculo), cpf_cliente)
                if veiculo.adicionar():
                    messagebox.showinfo("Sucesso", "✅ Cliente e veículo cadastrados com sucesso!")
                    self.limpar_campos()
                else:
                    messagebox.showerror("Erro", "❌ Erro ao cadastrar veículo. Placa pode já existir.")
            else:
                messagebox.showerror("Erro", "❌ Erro ao cadastrar cliente. CPF pode já existir.")
                
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro inesperado: {e}")

    def limpar_campos(self):
        for entry in [
            self.entry_nome, self.entry_cpf, self.entry_telefone, self.entry_email, self.entry_endereco,
            self.entry_marca, self.entry_modelo, self.entry_placa, self.entry_ano, self.entry_km
        ]:
            entry.delete(0, tk.END)
        self.entry_km.insert(0, "0")