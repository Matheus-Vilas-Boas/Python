km = float(input('Dígite a quantia de quilometros percorrido: '))
dias = int(input('Dígite a quantia de dias: '))

preço = km * 0.15 + dias * 60
print('O preço a ser pago é de R$ {:.2f}'.format(preço))
