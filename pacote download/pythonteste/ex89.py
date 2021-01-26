from time import sleep
ficha = list()
while True:
    nome = str(input('Digite seu nome: ')).strip()
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1 , nota2], media])
    resp = str(input('Do you wish to continue? [Y/N] ')).strip().upper()[0]
    if resp == 'Y':
        continue
    else:
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*32)
    opc = int(input('which student want to show the grade? [999 Stop]'))
    if opc == 999:
        print('Finishing...')
        sleep(1)
        break
    elif opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('-='*30)
print('Volte sempre!')
