preço = float(input('Dígite o preço do produto: '))
desconto = 0.05
novoPreço = preço - (preço * desconto)
print(f'O produto custa R${preço:.2f} e com desconto de 5% custa R${novoPreço:.2f}')
