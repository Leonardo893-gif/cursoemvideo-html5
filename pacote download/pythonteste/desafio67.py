tabuada = 0
valor = int(input('Tabuada do número: '))
while True:
    tabuada += 1
    print(f'{valor} x {tabuada} = {valor*tabuada}')
    if tabuada > 10:
        valor = int(input('Número: '))
        tabuada = 0
        if valor < 0:
            break
        continue
print('Fim da tabuada')
