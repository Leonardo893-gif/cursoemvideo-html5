preço = int(input('Qual é a distância da sua viagem em Km? '))
calculo = preço * 0.50
total = preço * 0.45
if preço <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(calculo))
else:
    print('A sua passagem custará R${:.2f}'.format(total))