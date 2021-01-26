adição = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador = contador + 1
        adição = adição + n
print('A soma de todos os {} números ímpares é de {}'.format(contador, adição))