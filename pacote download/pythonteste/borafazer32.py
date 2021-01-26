from datetime import date
temporada = int(input('Digite o ano que você quer analisar, Digite 0 para analisar o ano atual: '))
if temporada == 0:
    temporada = date.today().year
if temporada % 4 == 0 and temporada % 100 != 0 or temporada % 400 == 0:
     print('O ano de {} é um ano BISSEXTO!'.format(temporada))
else:
     print('O ano de {} não é um ano BISSEXTO!'.format(temporada))