salário = float(input('Qual é seu salário? '))
aumento = salário + (salário * 10 / 100)
aumento2 = salário + (salário * 15 / 100)
if salário >=1250.00:
    print('Quem ganhava {},Com o aumento de 10% vai ganhar agora {}'.format(salário, aumento))
else:
    print('Quem ganhava {},Com o aumento de 15% passa a ganhar agora {}'.format(salário, aumento2))