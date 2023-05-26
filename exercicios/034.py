salário = float(input('Qual o salário: '))
if (salário > 1250):
    print("O empregado ganhará 10% de desconto.")
    novoSalário = salário + (salário * 0.10)
    print(f'O novo salário é: {novoSalário:.2f}')
else:
    print('O empregado ganhará 15% de desconto.')
    novoSalário = salário + (salário * 0.15)
    print('O novo salário do empregado é de: {}'.format(novoSalário))