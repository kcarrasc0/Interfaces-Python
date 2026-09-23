import tkinter as tk

# 1. Cria a Janela Principal
janela = tk.Tk()
janela.geometry("300x200")

# 2. Cria os Widgets (Ainda invisíveis)
titulo = tk.Label(janela, text="Bem-vindo ao Sistema!")
campo_nome = tk.Entry(janela)
botao_enviar = tk.Button(janela, text="Enviar Dados")

# 3. Define o Layout (Coloca os itens na tela)
titulo.pack(pady=10)       # Empilha com espaço de 10px em cima e embaixo
campo_nome.pack(pady=5)
botao_enviar.pack(pady=15)

# 4. Inicia o Loop de Eventos (Mantém aberto)
janela.mainloop()