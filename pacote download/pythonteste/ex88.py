from random import randint
from time import sleep
lista = list()
jogos = list()
print('-='*30)
print('JOGO NA MEGA SENA')
print('-='*30)
quant = int(input('Quantos jogos você deseja que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 61)
        if n not in lista:
            lista.append(n)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='* 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, a in enumerate(jogos):
    print(f'Jogo {i+1}: {a}')
    sleep(1)
print('BOA SORTE!')
