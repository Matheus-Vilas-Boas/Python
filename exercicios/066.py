num = soma = cont = 0
while True:
    num = int(input('Enter a number: '))
    if num == 999:
        break
    soma +=num
    cont +=1
print(f'A soma dos valores {soma}')
print(f'A quantidade de valores digitados {cont}')

