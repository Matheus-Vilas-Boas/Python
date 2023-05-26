num = int(input('Dígite um número: '))
total = 0
for j in range(1, num + 1):
    if num % j == 0:
        total += 1
    else:
        print(f'{j}')
print(f'\n\033[m O número {num} foi divisível {total} vezes')

if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
