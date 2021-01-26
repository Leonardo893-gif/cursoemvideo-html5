valor = [[], []]
for s in range(1, 8):
    valores = int(input('Digite um número: '))
    if valores % 2 == 0:
        valor[0].append(valores)
    else:
        valor[1].append(valores)
print('=' * 30)
print(f'Números Pares: {sorted((valor[0]))}')
print(f'Ímpares: {sorted(valor[1])}')
