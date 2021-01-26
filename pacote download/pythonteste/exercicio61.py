n = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
termo = n
cont = total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        cont += 1
    print('Stop')
    mais = int(input('Quantos termos você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
