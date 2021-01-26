def verde():

    print('\033[0;30;46m', end='')

def branco():

    print('\033[7;30m', end='')

def azul():

    print('\033[0;30;44m', end='')

def vermelho():

    print('\033[0;30;41m', end='')

while True:
    verde()
    print('Welcome')
    f = str(input("Digite um comando: "))
    if f == 'fim':
        break

    else:

        vermelho()
        print(f'Acessando o manual de {f}')

        branco()

        s =  help(f)
verde()
print('Até a próxima!')
