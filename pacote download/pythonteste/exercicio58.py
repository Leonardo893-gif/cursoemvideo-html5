from random import randint
Computador = randint(0, 10) #computador vai pensar
print('Pensei em número de 0 a 10...')
print('Você consegue adivihar? ')
ganhou = False
chances = 0
while not ganhou:
    Jogador = int(input('Digite um número: '))
    chances += 1
    if Jogador == Computador:
        ganhou = True
    else:
        if Jogador < Computador:
            print('Tente um número maior')
        elif Jogador > Computador:
            print('Tente um número menor')
print('Você teve {} tentativas para acertar'.format(chances))
