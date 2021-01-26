from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
     ano = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
     idade = atual - ano
     if idade >= 21:
         totmaior += 1
     else:
         totmenor += 1
print('\033[0;36mAo todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('\033[0;32mE Também tivemos {} pessoas menores de idade'.format(totmenor))
