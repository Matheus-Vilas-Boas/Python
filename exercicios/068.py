from random import randint

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador} total: {total}' )
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você Venceu!')
    else:
        print('Opção inválida!')
print('GAME OVER!')
