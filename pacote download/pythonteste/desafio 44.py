valor = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] á vista no dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é sua opção? '))
if opção == 1:
    total = valor - (valor * 10 / 100)
elif opção == 2:
    total = valor - (valor * 5 / 100)
elif opção == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    juros = int(input('Em Quantas parcelas? '))
    parcelas = total / juros
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(juros, parcelas))
else:
    total = valor
    print('\033[0;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
