import tkinter as tk
from PIL import Image, ImageTk
from duelo import duelo


class RPGDuelGUI:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.carregar_background()
        self.carregar_widgets_iniciais()

    def configurar_janela(self):
        self.root.title("Mestre dos Duelos RPG")
        largura_janela = 800
        altura_janela = 800
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_central = int((largura_tela - largura_janela) / 2)
        y_central = int((altura_janela - largura_janela) / 2)
        self.root.geometry(f"{largura_janela}x{largura_janela}+{x_central}+{y_central}")
        self.root.resizable(False, False)

    def carregar_background(self):
        self.bg_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

    def carregar_widgets_iniciais(self):
        self.start_image = ImageTk.PhotoImage(Image.open("assets/start_button.png").resize((100, 100)))

        self.botao_iniciar = tk.Button(
            self.root,
            image=self.start_image,
            command=self.mostrar_campos_duelo,
            bg="#2b2b2b",
            bd=0,
            relief="flat",
            highlightthickness=0,
            activebackground="#2b2b2b",
        )
        self.botao_iniciar.place(relx=0.5, rely=0.9, anchor="center")

        self.frame_entradas = tk.Frame(self.root, bg="#2b2b2b")
        self.frame_entradas.place_forget()
        self.resultado_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.resultado_frame.place_forget()

    def mostrar_campos_duelo(self):
        self.botao_iniciar.place_forget()
        self.criar_entradas()
        self.criar_botao_duelo()

    def criar_entradas(self):
        self.frame_entradas.place(relx=0.5, rely=0.4, anchor="center")

        self.lutador1_nome = self.criar_campo(self.frame_entradas, "Nome do Lutador 1", 0, 0, valor_inicial="Thor")
        self.lutador1_classe = self.criar_campo(self.frame_entradas, "Classe do Lutador 1", 1, 0, valor_inicial="Guerreiro")
        self.lutador1_vida = self.criar_campo(self.frame_entradas, "Vida do Lutador 1", 2, 0, valor_inicial="100")
        self.lutador1_poder = self.criar_campo(self.frame_entradas, "Poder do Lutador 1", 3, 0, valor_inicial="20")

        self.lutador2_nome = self.criar_campo(self.frame_entradas, "Nome do Lutador 2", 0, 2, valor_inicial="Gandalf")
        self.lutador2_classe = self.criar_campo(self.frame_entradas, "Classe do Lutador 2", 1, 2, valor_inicial="Mago")
        self.lutador2_vida = self.criar_campo(self.frame_entradas, "Vida do Lutador 2", 2, 2, valor_inicial="80")
        self.lutador2_poder = self.criar_campo(self.frame_entradas, "Poder do Lutador 2", 3, 2, valor_inicial="25")

    def criar_campo(self, parent, texto, row, col, valor_inicial=""):
        label = tk.Label(parent, text=texto, font=("Helvetica", 12), bg="#2b2b2b", fg="#FFD700")
        label.grid(row=row, column=col, padx=10, pady=5, sticky="w")

        entry = tk.Entry(
            parent,
            font=("Helvetica", 12),
            width=20,
            bg="#1E1E1E",
            fg="#FFD700",
            insertbackground="#FFD700",
            highlightthickness=2,
            highlightbackground="#FFD700",
            highlightcolor="#FFEA00",
        )
        entry.grid(row=row, column=col + 1, padx=10, pady=5)
        entry.insert(0, valor_inicial)
        return entry

    def criar_botao_duelo(self):
        icon_image = ImageTk.PhotoImage(Image.open("assets/fight.png").resize((40, 40)))

        self.botao_duelo = tk.Button(
            self.root,
            text=" Iniciar Duelo",
            font=("Helvetica", 16, "bold"),
            image=icon_image,
            compound="left",
            bg="#000000",
            fg="#FFD700",
            activebackground="#388E3C",
            activeforeground="#FFD700",
            command=self.iniciar_duelo,
            padx=20,
            pady=10,
            bd=0,
            relief="flat",
        )
        self.botao_duelo.image = icon_image
        self.botao_duelo.place(relx=0.5, rely=0.7, anchor="center")

    def iniciar_duelo(self):
        try:
            lutador1 = {
                "nome": self.lutador1_nome.get(),
                "classe": self.lutador1_classe.get(),
                "vida": int(self.lutador1_vida.get()),
                "poder": int(self.lutador1_poder.get()),
            }

            lutador2 = {
                "nome": self.lutador2_nome.get(),
                "classe": self.lutador2_classe.get(),
                "vida": int(self.lutador2_vida.get()),
                "poder": int(self.lutador2_poder.get()),
            }

            vencedor = duelo(lutador1, lutador2)
            self.ocultar_campos()
            self.mostrar_mensagem(f"✨ O vencedor é: {vencedor} 🏆 ✨", "#FFD700")
            self.root.after(3000, self.reiniciar_tela)

        except ValueError:
            self.mostrar_mensagem("⚠️ Erro: Por favor, insira valores válidos! ⚠️", "#FF0000")
        except Exception as e:
            self.mostrar_mensagem(f"⚠️ Erro inesperado: {e} ⚠️", "#FF0000")

    def ocultar_campos(self):
        self.frame_entradas.place_forget()
        if hasattr(self, "botao_duelo"):
            self.botao_duelo.place_forget()

    def reiniciar_tela(self):
        if hasattr(self, "mensagem_vitoria"):
            self.mensagem_vitoria.destroy()
        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        self.botao_iniciar.place(relx=0.5, rely=0.9, anchor="center")

    def mostrar_mensagem(self, texto, cor):
        self.resultado_frame.place_forget()

        self.mensagem_vitoria = tk.Label(
            self.root,
            text=texto,
            font=("Helvetica", 32, "bold"),
            fg=cor,
            bg="#2b2b2b",
            relief="raised",
            padx=20,
            pady=10,
        )
        self.mensagem_vitoria.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    root = tk.Tk()
    app = RPGDuelGUI(root)
    root.mainloop()
