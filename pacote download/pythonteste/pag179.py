nomes = ['Ana', 'Carlos', 'Maria']
try:
    i = int(input('Digite o índice que você quer imprimir: '))
    print(nomes[i])
except ValueError as e:
    print('Digite um número!')
    raise
finally:
    print(f'Sempre o finally é executado')
