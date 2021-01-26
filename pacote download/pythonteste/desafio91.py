from random import randint
from operator import itemgetter
from time import sleep
dados = {}
cont1 = 1
cont = 0
while True:
    j = 'Jogador' + str(cont1)
    num = randint(1, 6)
    dados.update({j:num})
    cont1 += 1
    cont += 1
    print(f'O {j} tirou {num} no dado.')
    sleep(1)
    if cont == 4:
        break
c = 1
print('-'*30)
print(' == RANKING DOS JOGADORES  == ')
for item in sorted(dados, key=itemgetter(1), reverse=True):
    print(f'    {c}°lugar: {item} com {dados[item]}')
    c += 1
    sleep(1)
    