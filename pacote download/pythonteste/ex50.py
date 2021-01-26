soma = 0
cont = 0
for p in range(1, 7):
    par = int(input('Digite o {} número: ' .format(p)))
    if par % 2 == 0:
        soma = soma + par
        cont = cont + 1
print('Você Informou {} números e a soma dos números PARES é de {}'.format(cont, soma))