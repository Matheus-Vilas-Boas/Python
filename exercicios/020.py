from random import shuffle
n1 = str(input('Nome:'))
n2 = str(input('Nome:'))
n3 = str(input('Nome:'))
n4 = str(input('Nome:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'Os alunos escolhidos foram {lista}')
