print('='*30)
print('{:^30}'.format('Banco Leonardo'))
print('='*30)
saque = int(input('Valor do saque: R$'))
cedulas = [1, 10, 20, 50]
c = 3
while saque > 0:
    qntced = saque // cedulas[c]
    saque = saque - qntced * cedulas[c]
    if qntced > 0:
        print(f'{qntced} cedulas de R${cedulas[c]}')
    c -= 1
print('='*30)
print('Volte sempre ao nosso banco!')
