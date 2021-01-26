while True:
    numero = int(input('Tabuada do número: '))
    if numero < 0:
        break
    print('-'*30)
    for t in range(1, 11):
        print(f'{numero} x {t} = {numero*t}')
    print('-'*30)
print('Fim da tabuada')
