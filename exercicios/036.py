casa = float(input('Valor da casa: '))
salário = float(input('Salátio do comprador: '))
anos = int(input('Anos de financiamento: '))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar a casa de R${casa :.2f} em {anos} anos.\n')
print(f'a prestação será de {prestação :.2f}')
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
