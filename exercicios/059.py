n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
op = int(input('Sua opção: '))
while op != 5:
    if op == 1:
        s = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {s}')
    elif op == 2:
        m = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {m}')
    elif op == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
    else:
        print('Opção inválida. Tente novamente.')

    
