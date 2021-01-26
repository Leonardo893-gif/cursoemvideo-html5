lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!')
    else:
        print('Você já digitou esse número!')
    chamar = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if chamar == 'S':
        continue
    else:
        break
print('='* 40)
print(f'Você digitou os números {sorted(lista)}')
