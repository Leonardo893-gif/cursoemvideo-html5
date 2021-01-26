def leiaint(num):
    ok = False
    value = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0:31m Erro! Enter an integer\033[m')
        if ok:
            break
    return value


n = leiaint('Enter a value: ')
print(f'Você digitou o number {n}')
