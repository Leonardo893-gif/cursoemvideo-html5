casa = float(input('Qual é o preço da casa?R$' ))
salário = float(input('Qual é seu salário?R$ '))
anos = int(input('Quantos anos de financiamento? '))
conta = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(conta))
if conta <= minimo:
    print('Empréstimo pode ser CONCEDIDIO!')
else:
    print('Empréstimo NEGADO!')
