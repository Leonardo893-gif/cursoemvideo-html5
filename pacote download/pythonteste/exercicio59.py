from time import sleep
n = float(input('Digite um valor: '))
num = float(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''Você pode
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual sua escolha? '))
    if opção == 1:
        soma = n + num
        print('Somando {} + {} o resultado é {}'.format(n, num, soma))
    elif opção == 2:
        multiplicar = n * num
        print('Multiplicando {} x {} o resultado é {}'.format(n, num, multiplicar))
    elif opção == 3:
        if n > num:
            maior = n
            print('O maior número é {}'.format(maior))
        else:
            maior = num
            print('O maior número é {}'.format(maior))
    elif opção == 4:
        n = int(input('Digite outro número: '))
        num = int(input('Digite o segundo: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Erro, tente novamente')
        sleep(1)
print('Volte sempre!')
