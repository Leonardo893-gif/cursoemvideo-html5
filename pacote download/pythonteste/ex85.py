numeros = [[], []]
for n in range(1, 8):
    num = int(input('Qual número? '))
    if num % 2 == 1:
        numeros[0].append(num)
    elif num % 2 == 0:
        numeros[1].append(num)
print('-='*30)
print(f"Números Ímpares são: {sorted((numeros[0]))}")
print(f"Números pares: {sorted((numeros[1]))}")
