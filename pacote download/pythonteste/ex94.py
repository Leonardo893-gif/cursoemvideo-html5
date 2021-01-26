i = 0
pessoas = []
mulheres = []
while True:
    ficha = {}
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F':
       mulheres.append(nome)
    idade = int(input('Idade: '))
    i += idade
    resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    ficha['nome'] = nome
    ficha['sexo'] = sexo
    ficha['idade'] = idade
    pessoas.append(ficha.copy())
    if resposta == 'S':
        continue
    else:
        break
med = i / len(pessoas)
print('-='*30)
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'- A média de idade do grupo é {med} anos')
print('- As mulheres cadastradas foram: ',end=' ')
for m in range(0, len(mulheres)):
    print(mulheres[m], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ',end=' ')
print()
for m in range(0, len(pessoas)):
    if pessoas[m]['idade'] > med:
        print(f'nome = {pessoas[m]["nome"]}; sexo = {pessoas[m]["sexo"].upper()}; idade = {pessoas[m]["idade"]};')
print('>>>ENCERRADO>>>')
