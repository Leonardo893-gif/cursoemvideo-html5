print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
num = int(input('Digite um número para ver teu fibonacci: '))
c1 = 0
c2 = 1
print('~'*30)
cont = 3
print('{} -> {}'.format(c1, c2), end='')
while cont <= num:
    c3 = c1 + c2
    print('-> {}'.format(c3), end='')
    c1 = c2
    c2 = c3
    cont += 1
print('-> Fim')
print('~'*30)
