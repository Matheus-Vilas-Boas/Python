clubs = ('Botafogo', 'Grêmio', 'Flamengo','Palmeiras',  'Atlético-PR', 'São Paulo', 'Fluminense', 'Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Athletico-MG',  'Santos', 'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG', 'Vasco da Gama')



print(f'\nOs 5 primeiros colocados são: {clubs[0:5]}')
print(f'\nOs últimos 4 colocados são: {clubs[15:]}')
print(f'\nOs times em ordem alfabética: {sorted(clubs)}')



if clubs.count('São Paulo') > 0:
    print(f'\n O São Paulo FC está na {clubs.index("São Paulo") + 1}º posição')
else:
    print('\nO time do SPFC não está entre os 20 classificados.')

