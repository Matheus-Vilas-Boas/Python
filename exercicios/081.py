lista = []
cont = 0
contcinco = 0
print('-=' * 8 + '-')
while True:
    o = ' '
    cont += 1
    n = int(input(f'Digite o {cont}° número: '))
    if n == 5:
        contcinco += 1
    lista.append(n)
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if o == 'N':
        break
print('-=' * 8 + '-')
lista.sort(reverse=True)
print(f'Foram considerados \033[32m{cont}\033[m números.')
print(f'A lista invertida ficou: \033[32m{lista}\033[m')
if 5 in lista:
    print(f'O valor 5 foi digitado \033[32m{contcinco}\033[m vezes!')
else:
    print('O valor 5 não foi \033[32mnenhuma\033[m vez digitado')
print('-=' * 8 + '-')
