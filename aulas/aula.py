idade = [10,27,58,5,98,13,32,2,65,78,1,101]
menorIdade = idade[0]
maiorIdade = idade[0]

for idades in idade:
    if idades < menorIdade:
        menorIdade = idades
for idades in idade:
    if idades > maiorIdade:
        maiorIdade = idades

print(f"A menor idade: {menorIdade} e a maior idade: {maiorIdade}\n")

idade.sort
print(idade)
print(len(idade))