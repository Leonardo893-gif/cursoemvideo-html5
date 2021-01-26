print('--'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer? '))
c1 = 0
c2 = 1
print('~'*30)
print('{} -> {}'.format(c1, c2), end='')
cont = 3
while cont <= n:
    c3 = c1 + c2
    print('-> {}'.format(c3), end='')
    c1 = c2
    c2 = c3
    cont += 1
print('-> Fim')
print('~'*30)
