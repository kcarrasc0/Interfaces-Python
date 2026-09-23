import tkinter as tk
import random

LARGURA = 600
ALTURA = 600
TAMANHO_BLOCO = 20
VELOCIDADE_INICIAL = 120

COR_AZUL_PYTHON = "#3776AB"
COR_AMARELO_PYTHON = "#FFD43B"
COR_COMMIT = "#4CAF50" # Verde estilo GitHub
COR_FUNDO = "#1E1E1E" # Tema escuro (VS Code)

class JogoSnake:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Snake: Commit Arena")
        self.master.resizable(False, False)
        
        self.frame_menu = tk.Frame(self.master, bg=COR_FUNDO, width=LARGURA, height=ALTURA)
        self.frame_jogo = tk.Frame(self.master, bg=COR_FUNDO)
        
        self.iniciar_menu()

    def iniciar_menu(self):
        self.frame_jogo.pack_forget()
        self.frame_menu.pack()
        self.frame_menu.pack_propagate(False)

        titulo = tk.Label(self.frame_menu, text="SNAKE ARENA: COMMITS", font=("Consolas", 24, "bold"), fg="white", bg=COR_FUNDO)
        titulo.pack(pady=50)

        subtitulo = tk.Label(self.frame_menu, text="Escolha sua cobra:", font=("Consolas", 14), fg="white", bg=COR_FUNDO)
        subtitulo.pack(pady=20)

        btn_azul = tk.Button(self.frame_menu, text="Python Azul", font=("Consolas", 14, "bold"), bg=COR_AZUL_PYTHON, fg="white", width=20, command=lambda: self.preparar_jogo(COR_AZUL_PYTHON, COR_AMARELO_PYTHON))
        btn_azul.pack(pady=10)

        btn_amarela = tk.Button(self.frame_menu, text="Python Amarela", font=("Consolas", 14, "bold"), bg=COR_AMARELO_PYTHON, fg="black", width=20, command=lambda: self.preparar_jogo(COR_AMARELO_PYTHON, COR_AZUL_PYTHON))
        btn_amarela.pack(pady=10)

    def preparar_jogo(self, cor_jogador, cor_rival):
        self.cor_jogador = cor_jogador
        self.cor_rival = cor_rival
        
        self.frame_menu.pack_forget()
        self.frame_jogo.pack()

        self.pontos = 0
        self.nivel = 1
        self.velocidade = VELOCIDADE_INICIAL
        self.direcao = "Down"
        
        self.jogador_coords = [[60, 60], [60, 40], [60, 20]]
        self.rival_coords = []
        self.rival_ativo = False
        
        # Interface superior do jogo
        self.frame_painel = tk.Frame(self.frame_jogo, bg="#333333")
        self.frame_painel.pack(fill="x")
        
        self.label_placar = tk.Label(self.frame_painel, text=f"Commits: {self.pontos}  |  Nível: {self.nivel}", font=("Consolas", 14), bg="#333333", fg="white")
        self.label_placar.pack(pady=5)

        self.canvas = tk.Canvas(self.frame_jogo, bg=COR_FUNDO, width=LARGURA, height=ALTURA, highlightthickness=0)
        self.canvas.pack()

        self.master.bind("<Left>", lambda e: self.mudar_direcao("Left"))
        self.master.bind("<Right>", lambda e: self.mudar_direcao("Right"))
        self.master.bind("<Up>", lambda e: self.mudar_direcao("Up"))
        self.master.bind("<Down>", lambda e: self.mudar_direcao("Down"))

        self.desenhar_cobra(self.jogador_coords, self.cor_jogador, "jogador")
        self.gerar_commit()
        
        self.turno()

    def desenhar_cobra(self, coords, cor, tag):
        self.canvas.delete(tag)
        for x, y in coords:
            self.canvas.create_rectangle(x, y, x + TAMANHO_BLOCO, y + TAMANHO_BLOCO, fill=cor, tag=tag)

    def gerar_commit(self):
        # Corrigido com // (divisão inteira)
        x = random.randint(0, (LARGURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        y = random.randint(0, (ALTURA // TAMANHO_BLOCO) - 1) * TAMANHO_BLOCO
        self.commit_coord = [x, y]
        self.canvas.delete("commit")
        self.canvas.create_oval(x, y, x + TAMANHO_BLOCO, y + TAMANHO_BLOCO, fill=COR_COMMIT, tag="commit")

    def mudar_direcao(self, nova_direcao):
        opostas = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if nova_direcao != opostas.get(self.direcao):
            self.direcao = nova_direcao

    def mover_rival(self):
        if not self.rival_ativo:
            return

        x_cabeca, y_cabeca = self.rival_coords[0]
        x_commit, y_commit = self.commit_coord

        if x_cabeca < x_commit: x_cabeca += TAMANHO_BLOCO
        elif x_cabeca > x_commit: x_cabeca -= TAMANHO_BLOCO
        elif y_cabeca < y_commit: y_cabeca += TAMANHO_BLOCO
        elif y_cabeca > y_commit: y_cabeca -= TAMANHO_BLOCO

        self.rival_coords.insert(0, [x_cabeca, y_cabeca])
        
        if x_cabeca == x_commit and y_cabeca == y_commit:
            self.gerar_commit()
        else:
            self.rival_coords.pop()

        self.desenhar_cobra(self.rival_coords, self.cor_rival, "rival")

    def turno(self):
        x, y = self.jogador_coords[0]

        if self.direcao == "Up": y -= TAMANHO_BLOCO
        elif self.direcao == "Down": y += TAMANHO_BLOCO
        elif self.direcao == "Left": x -= TAMANHO_BLOCO
        elif self.direcao == "Right": x += TAMANHO_BLOCO

        self.jogador_coords.insert(0, [x, y])

        # Verifica se comeu o commit
        if x == self.commit_coord[0] and y == self.commit_coord[1]:
            self.pontos += 1
            if self.pontos % 3 == 0:
                self.nivel += 1
                self.velocidade = max(40, self.velocidade - 5)
                
                # Ativa o rival no nível 10
                if self.nivel == 10 and not self.rival_ativo:
                    self.rival_ativo = True
                    self.rival_coords = [[LARGURA-TAMANHO_BLOCO, ALTURA-TAMANHO_BLOCO], 
                                         [LARGURA-TAMANHO_BLOCO, ALTURA-(TAMANHO_BLOCO*2)], 
                                         [LARGURA-TAMANHO_BLOCO, ALTURA-(TAMANHO_BLOCO*3)]]

            self.label_placar.config(text=f"Commits: {self.pontos}  |  Nível: {self.nivel}")
            self.gerar_commit()
        else:
            self.jogador_coords.pop()

        self.desenhar_cobra(self.jogador_coords, self.cor_jogador, "jogador")
        
        # Movimenta o rival e checa se ele morreu
        if self.rival_ativo:
            self.mover_rival()
            if self.verificar_morte_rival():
                self.tela_vitoria("O rival sofreu um erro de sintaxe e bateu!\nVocê venceu!")
                return

        # Checa as vitórias ou derrotas do Jogador
        if self.verificar_colisoes():
            self.game_over()
        elif self.nivel >= 12: 
            # Se sobreviveu até o nível 12, vence o jogo!
            self.tela_vitoria("Você chegou ao Nível 12 e dominou o projeto!\nVocê venceu!")
        else:
            self.master.after(self.velocidade, self.turno)

    def verificar_colisoes(self):
        x, y = self.jogador_coords[0]

        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA: return True
        for corpo in self.jogador_coords[1:]:
            if x == corpo[0] and y == corpo[1]: return True
                
        if self.rival_ativo:
            for corpo in self.rival_coords:
                if x == corpo[0] and y == corpo[1]: return True

        return False

    def verificar_morte_rival(self):
        if not self.rival_ativo: return False
        x, y = self.rival_coords[0]
        
        # Rival bateu na parede
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA: return True
        # Rival bateu no próprio corpo
        for corpo in self.rival_coords[1:]:
            if x == corpo[0] and y == corpo[1]: return True
        # Rival bateu no jogador
        for corpo in self.jogador_coords:
            if x == corpo[0] and y == corpo[1]: return True
            
        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 - 50, font=("Consolas", 30, "bold"), text="MERGE CONFLICT!", fill="red")
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, font=("Consolas", 16), text=f"Você fez {self.pontos} commits no Nível {self.nivel}", fill="white")
        self.criar_botao_voltar()

    def tela_vitoria(self, motivo):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 - 60, font=("Consolas", 35, "bold"), text="MERGE APROVADO! 🎉", fill=COR_COMMIT)
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, font=("Consolas", 14), text=motivo, fill="white", justify="center")
        self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 + 40, font=("Consolas", 16), text=f"Total de Commits: {self.pontos}", fill="white")
        self.criar_botao_voltar(offset_y=90)

    def criar_botao_voltar(self, offset_y=60):
        btn_reiniciar = tk.Button(self.frame_jogo, text="Voltar ao Menu", font=("Consolas", 12), command=self.voltar_menu)
        self.canvas.create_window(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2 + offset_y, window=btn_reiniciar)

    def voltar_menu(self):
        self.frame_painel.destroy()
        self.canvas.destroy()
        self.iniciar_menu()

if __name__ == "__main__":
    raiz = tk.Tk()
    app = JogoSnake(raiz)
    raiz.mainloop()