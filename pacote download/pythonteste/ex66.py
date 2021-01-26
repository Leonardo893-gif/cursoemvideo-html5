n = 0
cont = 0
soma = 0
n = int(input('Digite um número: 999 para interromper'))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um número: 999 para interromper'))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
