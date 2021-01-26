soma = 0
cont = 0
for m in range(1, 501, 2):
    if m % 3 == 0:
        cont = cont + 1
        soma = soma + m
print('\033[0;34mA soma de todos os {} valores é {}'.format(cont, soma))
