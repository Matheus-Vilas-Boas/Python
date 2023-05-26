tot18 = tot20 = totH  = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo in 'Mm':
            totH += 1
        if sexo in 'Ff' and idade < 20:
            tot20 += 1        
        rep = ' '
        while rep not in 'SN':
            rep = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if rep == 'N':
                break
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {tot20} mulheres com menos de 20 anos')

