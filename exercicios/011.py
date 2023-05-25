altura = float(input('Dígite a altura em metros: '))
largura = float(input('Dígite a largura em metros: '))

parede = altura * largura
tinta = 2
area = parede / tinta
print(f'Sua parede tem {parede} m² e precisa de {area} litros de tinta.')