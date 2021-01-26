n = int(input('Digite o primeiro número: '))
num = int(input('Segundo: '))
numero = int(input('Terceiro: '))
quarto = int(input('Quarto: '))
guarde = n, num, numero, quarto
conta = n, num, numero, quarto / 2
print(f'Você digitou os números {guarde}')
print(f'O número 9 apareceu {guarde.count(9)} vezes')
if 3 in guarde:
    print(f'O valor 3 apareceu primeiro na {guarde.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu!')
for conta in guarde:
    if conta % 2 == 0:
        print(f'Os valores pares são {(conta)}')
for conta in guarde:
    if conta % 2 == 1:
        print(f'Os valores ímpares são {conta}')
