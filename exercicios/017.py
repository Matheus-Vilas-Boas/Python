import math

cO = float(input('Dígite o cateto oposto: '))
cA = float(input('Dígite o cateto adjacente: '))
print(f'O valor da hipotenusa é de {math.hypot(cO, cA)}')
