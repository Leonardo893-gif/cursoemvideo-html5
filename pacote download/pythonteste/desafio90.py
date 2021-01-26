aluno = {}
nome = str(input('Digite seu nome: ')).strip()
media = float(input(f'Informe sua média {nome}: '))
aluno['aluno'] = nome
aluno['media'] = media
print(f'Seu nome é {nome}')
print(f'Média é igual a {media}')
if media >= 7:
    print('Situação é igual a Aprovado(a)')
elif 5 <= aluno['media'] < 7:
    print('Situação é igual a Recuperação')
elif media < 4:
    print('Situação é igual a Reprovado(o)')
