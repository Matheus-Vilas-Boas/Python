frase = str(input('Escreva uma frase: ').upper())
print(f'A letra A apareceu {frase.count("A")} vezes')
print(f'A primeira ocorrencia foi {frase.find("A")+1}')
print(f'A última ocorrencia foi {frase.rfind("A")+1}')