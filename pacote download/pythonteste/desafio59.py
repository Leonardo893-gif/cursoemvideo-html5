from time import sleep
num = float(input('Digite o primeiro número: '))
n = float(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print(''' Escolha uma das opções
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual é sua opção: '))
    if opção == 1:
        soma = num + n
        print('A soma entre {} + {} é {}'.format(num, n, soma))
    elif opção == 2:
        multiplicação = num * n
        print('Multiplicando {} x {} o resultado é {}'.format(num, n, multiplicação))
    elif opção == 3:
        if num > n:
            maior = num
        else:
            maior = n
        print('Entre {} e {} o maior valor é {}'.format(num, n, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        num = int(input('Primeiro valor: '))
        n = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
    sleep(2)
print('Fim! Volte Sempre!')
