n = int(input('Digite um número: '))
total = 0
for num in range(1, n + 1):
    if n % num == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(num), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, total))
if total == 2:
    print('É um número Primo!')
else:
    print('Ele Não é um número Primo!')