import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from models.models import Manutencao, Veiculo

class ManutencaoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5F5F5")
        self.veiculo_map = {}
        self.criar_interface()

    def criar_interface(self):
        # Título
        titulo = tk.Label(self, text="Registro de Manutenção", font=("Arial Black", 18), bg="#F5F5F5")
        titulo.pack(pady=10)

        # Frame principal
        main_frame = tk.Frame(self, bg="#F5F5F5")
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Veículo
        tk.Label(main_frame, text="Veículo:*", bg="#F5F5F5", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.combo_veiculo = ttk.Combobox(main_frame, width=40, state="readonly", font=("Arial", 9))
        self.combo_veiculo.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

        # Data
        tk.Label(main_frame, text="Data:*", bg="#F5F5F5", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_data = tk.Entry(main_frame, width=30, font=("Arial", 9))
        self.entry_data.grid(row=3, column=0, sticky="w", pady=5)
        self.entry_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

        # Serviços
        tk.Label(main_frame, text="Serviços Realizados:*", bg="#F5F5F5", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", pady=(10,0))
        self.txt_servicos = tk.Text(main_frame, width=50, height=6, font=("Arial", 9))
        self.txt_servicos.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5)

        # Peças
        tk.Label(main_frame, text="Peças Utilizadas:", bg="#F5F5F5", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", pady=(10,0))
        self.txt_pecas = tk.Text(main_frame, width=50, height=4, font=("Arial", 9))
        self.txt_pecas.grid(row=7, column=0, columnspan=2, sticky="ew", pady=5)

        # Botão
        btn_frame = tk.Frame(main_frame, bg="#F5F5F5")
        btn_frame.grid(row=8, column=0, columnspan=2, pady=20)

        btn_registrar = tk.Button(btn_frame, text="Registrar Manutenção", command=self.registrar_manutencao,
                                  bg="#1976D2", fg="white", width=20, height=2, font=("Arial", 10, "bold"))
        btn_registrar.pack(pady=10)

        # Carregar veículos
        self.carregar_veiculos()

    def carregar_veiculos(self):
        veiculos = Veiculo.listar()
        if veiculos:
            veiculo_lista = [f"{v[1]} - {v[3]} ({v[6]})" for v in veiculos]
            self.veiculo_map = {display: v[1] for display, v in zip(veiculo_lista, veiculos)}
            self.combo_veiculo['values'] = veiculo_lista
        else:
            self.combo_veiculo['values'] = ["Nenhum veículo cadastrado"]

    def registrar_manutencao(self):
        veiculo_display = self.combo_veiculo.get()
        data = self.entry_data.get()
        servicos = self.txt_servicos.get("1.0", tk.END).strip()
        pecas = self.txt_pecas.get("1.0", tk.END).strip()

        if not veiculo_display or not data or not servicos:
            messagebox.showwarning("Atenção", "⚠️ Veículo, Data e Serviços são obrigatórios!")
            return

        try:
            placa_veiculo = self.veiculo_map.get(veiculo_display)
            if not placa_veiculo:
                messagebox.showerror("Erro", "❌ Veículo inválido!")
                return

            # Extrair modelo do veículo para o campo veic_manutencao
            modelo = veiculo_display.split(" - ")[1].split(" (")[0]

            manutencao = Manutencao(
                veic_manutencao=modelo,
                serv_manutencao=servicos,
                dta_manutencao=data,
                pecs_manutencao=pecas,
                placa_veiculo_manutencao=placa_veiculo
            )

            if manutencao.adicionar():
                messagebox.showinfo("Sucesso", "✅ Manutenção registrada com sucesso!")
                self.limpar_campos()
            else:
                messagebox.showerror("Erro", "❌ Erro ao registrar manutenção!")

        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro inesperado: {e}")

    def limpar_campos(self):
        self.combo_veiculo.set('')
        self.txt_servicos.delete("1.0", tk.END)
        self.txt_pecas.delete("1.0", tk.END)