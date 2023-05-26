somaIdade = 0
maioridade = 0
mediaidade = 0
homem = 0
nomevelho = ''
totalMulher20 = 0

for i in range(0, 4):
    print(f'---{i}° PESSOA---')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade
    if i == 0 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totalMulher20 += 1

mediaidade = somaIdade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}')
print(f'Ao todo são {totalMulher20} mulheres com menos de 20 anos')


