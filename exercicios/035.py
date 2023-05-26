num1 = int(input('Dígite um valor: '))
num2 = int(input('Dígite um valor: '))
num3 = int(input('Dígite um valor: '))

if num1 < num2 + num3 and num2 < num3 + num1 and num3 < num1 + num2:
    print('Os valores digitados formam um triângulo.')
else:
    print('Os valores digitados não formam um triângulo.')
