from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for cidadão in range(1, 8):
     ano = int(input('Em que ano a {}° pessoa nasceu?' .format(cidadão)))
     idade = atual - ano
     if idade >= 21:
        totalmaior += 1
     else:
        totalmenor += 1
print('Ao todo temos {} pessoas maiores de idade'.format(totalmaior))
print('{} são menores de idade'.format(totalmenor))