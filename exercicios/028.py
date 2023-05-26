from random import randint

computador = randint(0, 5)
print('Vou pensar em um número e você vai ter que adivinhar!')

jogador = int(input('Qual número você acha que pensei? '))

if jogador == computador:
    print('Você acertou!')
else:
    print(f'Você errou, eu pensei no número {computador}')