from time import sleep
from random import randint
dados = {}
cont1 = 0
cont2 = 1
while True:
    j = 'Jogador' + str(cont2)
    n = randint(1, 6)
    dados.update({j:n})
    cont1 += 1
    cont2 += 1
    print(f'O {j} jogou {n}')
    sleep(1)
    if cont1 == 4:
        break
c = 1
print('-='*30)
for item in sorted(dados, key=dados.get, reverse=True):
    print(f'{c}°colocado: {item} com {dados[item]}')
    c += 1
    sleep(1)
