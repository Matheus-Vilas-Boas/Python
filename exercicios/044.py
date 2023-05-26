preço = float(input('Preço do produto: R$ '))
print('''
[1] - À vista / cheque
[2] - À vista no cartão
[3] - 2x no cartão 
[4] - 3x ou mais no cartão
''')
opçao = int(input('Qual a opção de pagamento: '))
if opçao == 1:
    total = preço - (preço * 0.10)
    print('O valor total é de R$ {:.2f}'.format(total))
elif opçao == 2:
    total = preço - (preço * 0.05)
    print('O valor total é de R$ {:.2f}'.format(total))
elif opçao == 3:
    total = preço
    print('O valor total é de R$ {:.2f}'.format(total))
elif opçao == 4:
    total = preço + (preço * 0.20)
    print('O valor total é de R$ {:.2f}'.format(total))
else:
    print('Opção inválida')
    print('Tente novamente')
