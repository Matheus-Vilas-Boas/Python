kmh = int(input('Km/h: '))
if kmh > 80:
    print('Você está acima do limite permitido. MULTADO!')
    print(f'O valor da multa é de R${(kmh - 80)*7:.2f}')
else:
    print('Você está dentro do limite permitido.')
    print('Tenha um bom dia! Dirija com segurança!')
