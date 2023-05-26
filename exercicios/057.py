Sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F]')).upper().strip() 
print('Sexo {} registrado com sucesso!'.format(sexo))