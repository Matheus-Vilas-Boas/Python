idade = int(input('informe sua idade: '))
if idade < 18:
    print(f'você não pode se alsitar, ainda falta {18 - idade} anos(s)')
elif idade == 18:
    print('você pode se alsitar')
else:
    print(f'já passou da hora de alistar, cerca de {idade - 18} ano(s)')