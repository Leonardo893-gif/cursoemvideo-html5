lista = []
while True:
    numero = int(input('Digite um valor: '))
    resp = str(input('Continuar? (S/N) ')).upper().strip()[0]
    lista.append(numero)
    if resp == 'S':
        continue
    else:
        break
if 5 in lista:
    print(f'O número 5 foi digitado e está na lista na posição {lista.index(5) + 1}')
else:
    print('O 5 não apareceu na lista!')
lista.sort(reverse=True)
print(f'A lista possui {len(lista)} elementos')
print(f'Em ordem decrescente são {lista}')
