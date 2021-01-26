pessoa = dict()
pessoas = list()
s = media = 0
mulheres = []
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')) # Pergunta o nome
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]: ')).upper()[0].strip()
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite F ou M.')
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade'] # Está somando a idade
    pessoas.append(pessoa.copy()) # Faz uma cópia
    while True:
        resp = str(input('Continuar? [S/N]: ')).upper()[0].strip()
        if resp in 'SN':
            break
        print('Erro! Digite S ou N') # Se não for S ou N, ele dá erro e continua
    if resp == 'N':
        break
print('-='*30) # Da linha 23 pra baixo eu estou analisando os daos
print(f' A) {len(pessoas)} pessoas foram cadastradas') # Mostra a quantidade de pessoas cadastradas
media = s / len(pessoas) # Faz a média de idade
print(f' B) A média de idade do grupo é {media:5.2f} anos') # Mostra a idade do grupo
print(f' C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in "Ff": # Mostra as mulheres cadastradas
        print(f'{p["nome"]} ', end='')
print()
print(' D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media: # Verifica quem está acima da média
        print('    ',end='')
        for k, v in p.items():
            print(f" {k} = {v}; ", end=' ')
        print()
print('<< ENCERRADO >>')
