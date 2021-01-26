p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
décimo = p + (10 - 1) * r
for c in range(p, décimo + r, r):
    print('{}'.format(c), end='-> ')
print('ACABOU')