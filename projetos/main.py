import pandas as pd

# Carregue os dados do arquivo CSV em um DataFrame
dados = pd.read_csv("vendas.csv")

# Calcule a média das vendas
media_vendas = dados["Vendas"].mean()

print("A média das vendas é:", media_vendas)
