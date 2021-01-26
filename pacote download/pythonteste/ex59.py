from time import sleep
n = float(input('Informe um valor: '))
num = float(input('Informe o segundo valor: '))
alternativa = 0
while alternativa != 5:
    print('''Você tem as seguintes opções 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    alternativa = int(input('Qual você deseja? '))
    if alternativa == 1:
        soma = n + num
        print('A soma entre {} e {} é igual a {}'.format(n, num, soma))
    elif alternativa == 2:
        multiplicar = n * num
        print('Multiplicando {} x {} o total é igual a {}'.format(n, num, multiplicar))
    elif alternativa == 3:
        if n > num:
            maior = n
        else:
            maior = num
        print('Entre {} e {} o maior número é {}'.format(n, num, maior))
    elif alternativa == 4:
        n = float(input('Digite o primeiro número: '))
        num = float(input('Digite o segundo valor: '))
    elif alternativa == 5:
        print('Finalizando...')
    else:
        print('Opção incorreta, tente novamente')
    sleep(1)
print('Você saiu do programa, volte sempre!')
