lista = []
total = []
peso = []
while True:
    Nome = str(input('Nome: ')).strip()
    Peso = float(input('Peso: '))
    lista.append(Nome)
    lista.append(Peso)
    total.append(lista[:])
    peso.append(lista[1])
    lista.clear()
    resp = str(input('Continue? S/N ')).strip().upper()[0]
    if resp == 'S':
        continue
    else:
        break
print(f'{len(total)} pessoas foram cadastradas')
print(f'O Maior peso foi de {max(peso):.2f} Kg')
for p in total:
    if p[1] == max(peso):
        print(f'Peso de: {p[0]}')
print('-' * 30)
print(f'O Menor peso foi de {min(peso):.2f}Kg')
for p in total:
    if p[1] == min(peso):
        print(f'Peso de: {p[0]}')
print('Thank you!')
