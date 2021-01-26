matriz = [[], [], []]
somap = maior = scol = 0
for m in range(3):
    for e in range(3):
        matriz[e].append(int(input(f'Digite um valor [{m},{e}]:')))
print('='*30)
for c in range(len(matriz)):
    for z in range(len(matriz)):
         print(f'[{matriz[c][z]:^5}]', end='')
         if matriz[c] [z] % 2 == 0:
            somap += matriz[c][z]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somap}')
for c in range(0, 3):
    scol += matriz[c] [2]
print(f'Terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"Maior valor da 2° linha é {maior}.")
