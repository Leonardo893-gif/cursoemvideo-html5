from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
saldo = 18 - idade
calculo = idade - 18
ano = atual + saldo
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade,atual))
if idade == 18:
    print('\033[0;31mVocê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos!'.format(calculo))
    print('\033[0;34mSeu alistamento foi em {}'.format(ano))