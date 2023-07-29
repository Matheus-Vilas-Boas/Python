listagem = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20',
            'Compasso', '9.99', 'Mochila', '120.32', 'Caneta', '22.30', 'Livro', '34.90')

print('-'*90)
print('{:^90}'.format('\033[1;32mLISTAGEM DE PREÇOS\033[m'))
print('-'*90)

# for i in range(0, int(len(listagem)/2)+1):  Solução 1 - Achei muito complexo desse jeito e aí coloquei como comentário

print('\033[1;34m')
for i in range(0, len(listagem), 2): #  Solução 2 - Achei essa solução mais "elegante" como você diz 
    print(f'{listagem[i]:.<76}', 'R$', f'{listagem[i+1]:>10}')
print('\033[m')
print('-'*90)