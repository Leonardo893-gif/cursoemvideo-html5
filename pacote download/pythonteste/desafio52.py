numero = int(input('Digite um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divísivel {} vezes'.format(numero, total))
if total == 2:
    print('\033[0;36mE por isso é um número PRIMO!')
else:
    print('\033[0;31mE por isso NÃO é um número PRIMO!')
