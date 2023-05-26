num = 0
cont = 0
soma = 0
while num!= 999:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1;
print(f'Você digitou {cont} números e o maior número foi {max(num)} e o menor número foi {min(num)}.')
print(f'A soma dos números digitados foi {soma}.')
print('Fim')
