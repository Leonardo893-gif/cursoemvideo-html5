lista = []
peso = []
total = []
while True:
    nome = str(input('Digite seu nome: ')).strip()
    resp = float(input('Seu peso: '))
    lista.append(nome)
    lista.append(resp)
    total.append(lista[:])
    peso.append(lista[1])
    lista.clear()
    continuar = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if continuar != 'S':
        break
    else:
        continue
print(f'{len(total)} pessoas foram cadastradas')
print(f'Maior Peso: {max(peso)}')
for p in total:
    if p[1] == max(peso):
        print(f'Peso de: {p[0]}')
print('-='*30)
print(f'Menor peso: {min(peso)}Kg')
for p in total:
    if p[1] == min(peso):
        print(f'Peso de: {p[0]}')
