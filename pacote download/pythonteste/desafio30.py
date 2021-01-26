num = int(input('Digite um número inteiro: '))
resultado = num % 2
if resultado == 0:
    print('\033[0;33mNúmero {} é número PAR!\033[m'.format(num))
else:
    print('\033[7;30mNúmero {} é um Número ÍMPAR!\033[m'.format(num))
