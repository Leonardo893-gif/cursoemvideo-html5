lista_completa = []
Lista_Par = []
Lista_Ímpar = []
while True:
    Numeros = int(input('Digite um número: '))
    resposta = str(input('Continue? [S/N] ')).strip().upper()[0]
    lista_completa.append(Numeros)
    if Numeros % 2 == 0:
        Lista_Par.append(Numeros)
    elif Numeros % 2 == 1:
        Lista_Ímpar.append(Numeros)
    if resposta == 'S':
        continue
    else:
        break
print('='* 30)
print(f'\033[0:30mA lista completa é {lista_completa}')
print(f'\033[0;31mPares: {Lista_Par}')
print(f'\033[0;34mÍmpares: {Lista_Ímpar}')
