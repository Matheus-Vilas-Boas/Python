altura = float(input('Sua alturam em metros: '))
massa = float(input('Sua massa em kg: '))
imc = massa / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso normal')
elif 25 <= imc < 30:
    print('Você está acima do peso')
elif 30 <= imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')

