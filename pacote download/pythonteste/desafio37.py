n = int(input('Digite um número inteiro: '))
print('''Escolha qual das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(n, bin(n) [2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(n, oct(n) [2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(n, hex(n) [2:]))
else:
    print('\033[0;31mOpção inválida: Tente novamente!')