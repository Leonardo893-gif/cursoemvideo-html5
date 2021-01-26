matriz = [[], [], []]
for v in range(3):
    for s in range(3):
        matriz[s].append(int(input(f'Digite um número posição: [{v},{s}]:')))
print('-='*30)
for c in range(len(matriz)):
    for x in range(len(matriz)):
         print(f'[{matriz[c][x]:^7}]', end='')
    print()
