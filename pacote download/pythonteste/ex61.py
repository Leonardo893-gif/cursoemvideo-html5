num = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = num
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razão
        cont += 1
    print('Stop')
    mais = int(input('Quantos termos você quer? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
