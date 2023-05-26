from time import sleep
for cont in range(10, -1, -1):
    sleep(0.5)
    print(f'{cont}')
print('Acabou')