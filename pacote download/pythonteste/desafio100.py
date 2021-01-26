from random import randint
from time import sleep
def sorteio(num):
    guarde = list()


    for c in range(0, num):
        guarde.append(randint(0, 10))
    print(f'Sorteando {num} valores da lista: ', end='')
    for v in guarde:
        print(f'{v}', end=' ')
        sleep(1)
    print('PRONTO!')
    def pares(par):
        soma = 0
        for p in par:
            if p % 2 == 0:
                soma += p
        print(f'Somando os valores pares de {guarde}, temos: {soma}')
        print(f'Somando todos valores temos: {sum(guarde)}')
    pares(guarde)
sorteio(5)
