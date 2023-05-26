total = totmil = cont = menor = 0
while True:
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break
print(f'total da compra foi de R$ {total}')
print(f'{totmil} produtos custam mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {menor}')
