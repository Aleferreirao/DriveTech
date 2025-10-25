import tkinter as tk
from tkinter import messagebox
from database.database import criar_tabelas
from views.cadastro_frame import CadastroFrame
from views.manutencao_frame import ManutencaoFrame
from views.consulta_frame import ConsultaFrame

class HomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drive Tech - Sistema de Manutenção")
        self.root.geometry("1000x700")
        self.root.configure(bg="#F5F5F5")
        
        # Garantir que as tabelas existem
        try:
            criar_tabelas()
            print("✅ Sistema inicializado com sucesso!")
        except Exception as e:
            print(f"⚠️ Aviso: {e}")

        # Barra superior
        top_bar = tk.Frame(root, bg="#1E88E5", height=70)
        top_bar.pack(side="top", fill="x")
        top_bar.pack_propagate(False)

        logo = tk.Label(top_bar, text="DRIVE TECH", font=("Arial Black", 22), 
                       bg="#1E88E5", fg="white")
        logo.pack(side="left", padx=25, pady=15)

        usuario = tk.Label(top_bar, text="Olá, Usuário 👤", font=("Arial", 12), 
                          bg="#1E88E5", fg="white")
        usuario.pack(side="right", padx=25, pady=15)

        # Container principal
        main_container = tk.Frame(root, bg="#F5F5F5")
        main_container.pack(fill="both", expand=True)

        # Menu lateral
        menu = tk.Frame(main_container, bg="#2C2C2C", width=220)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        # Área principal
        self.main_panel = tk.Frame(main_container, bg="white")
        self.main_panel.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        # Botões do menu
        self.criar_botoes_menu(menu)

        # Tela inicial
        self.mostrar_inicio()

    def criar_botoes_menu(self, menu):
        def add_menu_button(text, command):
            btn = tk.Button(menu, text=text, command=command,
                          fg="white", bg="#2C2C2C", anchor="w", 
                          padx=20, pady=12, font=("Arial", 11),
                          relief="flat", bd=0, width=18)
            btn.pack(fill="x", pady=1)
            
            def on_enter(e):
                btn.config(bg="#37474F")
            def on_leave(e):
                btn.config(bg="#2C2C2C")
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

        # Título do menu
        tk.Label(menu, text="MENU", font=("Arial Black", 12), 
                bg="#2C2C2C", fg="white", pady=15).pack(fill="x")

        add_menu_button("🏠 Início", self.mostrar_inicio)
        add_menu_button("👥 Cadastrar Cliente/Veículo", self.abrir_cadastro)
        add_menu_button("🔧 Registrar Manutenção", self.abrir_manutencao)
        add_menu_button("📋 Consultar Clientes", lambda: self.abrir_consulta("clientes"))
        add_menu_button("🚗 Consultar Veículos", lambda: self.abrir_consulta("veiculos"))
        add_menu_button("📊 Consultar Manutenções", lambda: self.abrir_consulta("manutencoes"))
        add_menu_button("❌ Sair", self.sair)

    def limpar_main_panel(self):
        for widget in self.main_panel.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpar_main_panel()
        
        # Banner de boas-vindas
        welcome_frame = tk.Frame(self.main_panel, bg="white")
        welcome_frame.pack(expand=True, fill="both")
        
        tk.Label(welcome_frame, text="Bem-vindo ao Drive Tech!", 
                font=("Arial Black", 28), bg="white", fg="#1E88E5").pack(pady=30)
        
        tk.Label(welcome_frame, text="Sistema de Gerenciamento de Manutenção Veicular", 
                font=("Arial", 16), bg="white", fg="#666666").pack(pady=10)
        
        # Estatísticas
        stats_frame = tk.Frame(welcome_frame, bg="white")
        stats_frame.pack(pady=50)
        
        try:
            from models.models import Cliente, Veiculo, Manutencao
            total_clientes = len(Cliente.listar())
            total_veiculos = len(Veiculo.listar())
            total_manutencoes = len(Manutencao.listar())
            
            stats = [
                f"📊 Total de Clientes: {total_clientes}",
                f"🚗 Total de Veículos: {total_veiculos}", 
                f"🔧 Total de Manutenções: {total_manutencoes}"
            ]
            
            for stat in stats:
                tk.Label(stats_frame, text=stat, font=("Arial", 14), 
                        bg="white", fg="#333333").pack(pady=8)
                        
        except Exception as e:
            tk.Label(stats_frame, text="📊 Carregando estatísticas...", 
                    font=("Arial", 14), bg="white", fg="#333333").pack(pady=8)

    def abrir_cadastro(self):
        self.limpar_main_panel()
        try:
            frame = CadastroFrame(self.main_panel)
            frame.pack(expand=True, fill="both", padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao abrir cadastro: {e}")

    def abrir_manutencao(self):
        self.limpar_main_panel()
        try:
            frame = ManutencaoFrame(self.main_panel)
            frame.pack(expand=True, fill="both", padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao abrir manutenção: {e}")

    def abrir_consulta(self, tipo):
        self.limpar_main_panel()
        try:
            frame = ConsultaFrame(self.main_panel, tipo)
            frame.pack(expand=True, fill="both", padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erro", f"❌ Erro ao abrir consulta: {e}")

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja realmente sair do sistema?"):
            self.root.quit()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = HomeApp(root)
        root.mainloop()
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        messagebox.showerror("Erro Fatal", f"O aplicativo encontrou um erro:\n{e}")