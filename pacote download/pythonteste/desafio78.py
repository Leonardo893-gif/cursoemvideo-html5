numero = int(input('Digite um número: '))
n = int(input('Digite o segundo número: '))
num = int(input('3° número: '))
quarto = int(input('4° número: '))
quinto = int(input('5° número: '))
guardar = numero, n, num, quarto, quinto
print(f'Você digitou os números {guardar}')
print(f'\033[0;30mO Maior número é {max(guardar)} e esta nas: ')
for p, valor in enumerate(guardar):
    if valor == max(guardar):
        print(f'\033[3;32mPosições: {p}')
print(f'\033[1;31mO Menor valor é {min(guardar)} e esta nas: ')
for p, valor in enumerate(guardar):
    if valor == min(guardar):
        print(f'\033[2;34mPosições: {p}')
