brasileirao = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', \
              'Cruzeiro', 'Flamengo', 'Vasco da Gama','Chapecoense', 'Atlético MG', 'Botafogo', 'Athletico-PR', \
              'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'\n\033[2;30mTabela do Campeonato Brasileiro de 2017: {brasileirao}')
print('=-' * 40)
print(f'\n\033[3;34mOs 5 primeiros colocados são: {brasileirao[0:5]}')
print('=-' * 40)
print(f'\n\033[3;31mOs 4 últimos são: {brasileirao[16:20]}')
print('=-' * 40)
print(f'\n\033[5;33mTimes em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 40)
print(f'\033[1;35mA Chapecoense está na 8° posição')
