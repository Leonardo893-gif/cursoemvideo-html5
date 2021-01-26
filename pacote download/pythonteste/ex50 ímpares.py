resto = 0
for i in range(1, 7):
    impar = int(input('Digite o {} número: ' .format(i)))
    if impar % 3 == 1:
        resto = resto / impar
print('A soma é de {}'.format(resto))