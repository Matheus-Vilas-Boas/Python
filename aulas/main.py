import tkinter as tk

# Cria uma instância da janela principal
janela = tk.Tk()
janela.title("Informações")

# Função para criar e estilizar um rótulo em um bloco
def criar_rotulo_no_bloco(bloco, texto, cor):
    frame = tk.Frame(bloco, bg=cor, padx=10, pady=10)
    frame.pack(fill="both", expand=True)
    rotulo = tk.Label(frame, text=texto, font=("Arial", 12))
    rotulo.pack(fill="both", expand=True)

# Crie 4 frames para representar os 4 blocos
bloco1 = tk.Frame(janela)
bloco2 = tk.Frame(janela)
bloco3 = tk.Frame(janela)
bloco4 = tk.Frame(janela)

# Configure o layout de grade para os blocos
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

# Coloque os blocos na janela usando o layout de grade
bloco1.grid(row=0, column=0, sticky="nsew")
bloco2.grid(row=0, column=1, sticky="nsew")
bloco3.grid(row=1, column=0, sticky="nsew")
bloco4.grid(row=1, column=1, sticky="nsew")

# Defina as informações e as cores correspondentes para cada bloco
informacoes = [
    ("Geolocalização:\nLatitude: 40.7128\nLongitude: -74.0060", "lightblue"),
    ("Altura: 100 metros", "lightgreen"),
    ("Batimentos: 72 bpm", "lightpink"),
    ("Queda: 9.8 m/s²", "lightyellow")
]

# Crie e estilize os rótulos com base nas informações em cada bloco
for i, (texto, cor) in enumerate(informacoes):
    if i == 0:
        criar_rotulo_no_bloco(bloco1, texto, cor)
    elif i == 1:
        criar_rotulo_no_bloco(bloco2, texto, cor)
    elif i == 2:
        criar_rotulo_no_bloco(bloco3, texto, cor)
    elif i == 3:
        criar_rotulo_no_bloco(bloco4, texto, cor)

# Inicia o loop principal da interface gráfica
janela.mainloop()
