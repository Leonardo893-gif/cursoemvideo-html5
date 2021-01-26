from time import sleep
from datetime import datetime
while True:
    nome = str(input('Nome: ')).strip()
    ano = int(input('Ano de nascimento: '))
    ctps = int(input('Número da carteira de trabalho: (0 não tem!) '))
    if ctps == 0:
        break
    anocontratacao = int(input('Ano de contratação: '))
    if anocontratacao < ano:
        print('Erro! Digite valores válido por favor!')
        continue
    elif anocontratacao == ano:
        print(f'Digite valores válidos!')
        continue
    Salário = float(input('Salário  R$: '))
    break
if ctps == 0:
    dados = {
        'nome': nome,
        'idade': datetime.today().year - ano,
        'ctps': ctps
    }
else:
    dados = {
        'nome tem o valor': nome,
        'idade tem o valor': datetime.today().year - ano,
        'ctps tem o valor': ctps,
        'anocontratação tem o valor': anocontratacao,
        'salário tem o valor': Salário,
        'aposentadoria tem o valor': anocontratacao + 35 - ano
    }
for k, i in dados.items():
    print(f'{k} - {i}')
    sleep(1.2)
