nome = str(input('Nome: '))
print(nome.upper())
print(len(nome))
primeiroNome = nome.split()
print (f'Seu primeiro nome tem {len(primeiroNome[0])} letras')