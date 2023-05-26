num1 = int(input('Dígite um número: '))
num2 = int(input('Dígite um número: '))
num3 = int(input('Dígite um número: '))

menor = 0
maior = 0

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3:
    menor = num2
else:
    menor = num3

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3
    
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
