from random import randint
computador = randint(0, 10) # computador pensa
print('Acabei de pensar em número de 0 e 10.')
print('Será que voce consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Você acertou com {} tentativa(s)!'.format(palpites))
