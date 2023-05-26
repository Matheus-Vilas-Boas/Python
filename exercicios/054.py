menor = 0
maior = 0
for i in range(0, 7):
    nas = int(input('Seu ano de nascimento:'))
    idade = 2023 - nas
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f'O número de pessoas maior de idade é {maior}')
print(f'O número de pessoas menor de idade é {menor}')