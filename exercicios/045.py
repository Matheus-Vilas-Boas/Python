from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
IAs = randint(0, 2)
print('-' * 30)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-' * 30)
jogador = int(input('Qual é a sua jogada? '))
print(f'O computador jogou {itens[IAs]}')
print(f'Você jogou {itens[jogador]}')
print('-' * 30)
if jogador == IAs:
    print('Empate!')
elif jogador == 0 and IAs == 1:
    print('Você perdeu!')
elif jogador == 0 and IAs == 2:
    print('Você ganhou!')
elif jogador == 1 and IAs == 0:
    print('Você ganhou!')
elif jogador == 1 and IAs == 2:
    print('Você perdeu!')
elif jogador == 2 and IAs == 0:
    print('Você perdeu!')
elif jogador == 2 and IAs == 1:
    print('Você ganhou!')
else:
    print('Jogada Inválida!')
    print('-' * 30)
