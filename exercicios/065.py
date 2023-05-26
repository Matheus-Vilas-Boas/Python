resp = 'S'
soma = quantia = média = 0
while resp in 'Ss':
    num = int(input('Dígite um número: '))
    soma = soma + num
    quantia = quantia + 1
    if quantia == 1:
        maior = menor = num
    else:
        if num < maior:
            maior = num
        if num > menor:
            menor = num
        
    resp = str(input('Quer continuar?[S/N]')).upper().strip()
média = soma / quantia
print(f'Você digitou {quantia} números e a média entre eles é {média}')
print('FIM')
