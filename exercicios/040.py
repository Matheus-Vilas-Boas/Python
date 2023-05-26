nota1 = float(input("NP1 = "))
nota2 = float(input("NP2 = "))

NF = (nota1 + nota2) / 2

print(f'A média entre as notas foi de {NF}')

if NF < 5:
    print("REPROVADO")
elif NF >= 5 or NF <=6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
