casa = float(input('Qual é o valor da casa que quer financiar? R$ '))
salário = float(input('Qual é seu salário?R$ '))
anos = int(input('Em Quantos anos você pretende pagar a casa? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A Prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
