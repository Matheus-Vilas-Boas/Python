km = float(input('Quatos km é a viajem? '))

if km <= 200:
    preco = km * 0.50
    print(f'O preço da viagem é de R$ {preco:.2f}')
else:
    preco = km * 0.45
    print(f'O preço da viagem é de R$ {preco:.2f}')
