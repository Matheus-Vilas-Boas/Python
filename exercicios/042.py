num1 = int(input('Dígite um valor: '))
num2 = int(input('Dígite um valor: '))
num3 = int(input('Dígite um valor: '))

if num1 < num2 + num3 and num2 < num3 + num1 and num3 < num1 + num2:
    print('Os valores digitados formam um triângulo.')
elif num1 == num2 == num3:
    print('Os valores digitados formam um triângulo equilátero.')
elif num1 != num2 == num3:
    print('Os valores digitados formam um triângulo escaleno.')
elif num3 != num2 != num1:
    print('Os valores digitados formam um triângulo isósceles.')
else:
    print('Os valores digitados não formam um triângulo.')