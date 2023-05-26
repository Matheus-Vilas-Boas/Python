num = int(input('Dígite um valor: '))
const = int(input('Dígite sua constante: '))
décimo = num + (10 - 1) * const

for i in range(num, décimo + const, const):
    print(i)
