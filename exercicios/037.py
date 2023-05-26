num = int(input('Dígite um número inteiro: \n'))
print('''Dígite para converter:
[1](Binário) 
[2](octal) 
[3] hexadecimal) :''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O número {num} em binário é: {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num} em octal é: {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} em hexadecimal é: {hex(num)[2:]}')
else:
    print('Valor incorreto!')
