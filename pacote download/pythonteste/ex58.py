from random import randint
computador = randint(0, 10) #tente adivinhar
print('Pensei em um número de 0 a 10')
print('Tente adivinhar...')
ganhou = False
chances = 0
while not ganhou:
    jogador = int(input('Digite um valor: '))
    chances += 1
    if jogador == computador:
        ganhou = True
    else:
        if jogador < computador:
            print('Tente um número maior')
        elif jogador > computador:
            print('Tente um número menor')
print('Você acertou com {} tentativa(s)'.format(chances))
