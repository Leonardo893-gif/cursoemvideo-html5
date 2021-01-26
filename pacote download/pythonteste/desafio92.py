from datetime import datetime
while True:
    nome = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    carteira = int(input(f'Número da Carteira de Trabalho do {nome}: Atenção! (0 não tem!) '))
    if carteira == 0:
        break
    anocontratação = int(input('Ano de Contratação: '))
    if anocontratação < ano:
        print('Digite valores válidos!')
        continue
    Salario = float(input('Salário R$: '))
    break
if carteira == 0:
    dados = {
        'nome tem o valor': nome,
        'idade tem o valor': datetime.today().year - ano,
        'ctps tem o valor': carteira
    }
else:
    dados = {
        'nome tem o valor': nome,
        'idade tem o valor': datetime.today().year - ano,
        'ctps tem o valor': carteira,
        'anocontratação tem o valor': anocontratação,
        'salário tem o valor': Salario,
        'aposentadoria tem o valor': anocontratação+35-ano
    }
for k, v in dados.items():
    print(f'{k} - {v}')
    