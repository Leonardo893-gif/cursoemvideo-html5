from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    escolha = str(input("Continuar? [S/N] ")).strip().upper()[0]
    if escolha == 'S':
        continue
    else:
        break
print('-='*39)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? [999 para parar]'))
    if opc == 999:
        print('Finalizando...')
        sleep(2)
        break
    elif opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('-='*30)
