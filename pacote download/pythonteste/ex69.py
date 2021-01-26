print('-'*30)
print('Seja bem vindo')
print('-'*29)
contadordemulheres = 0
contadordehomens = 0
contadordeidade = 0
contadordepessoas = 0
while True:
    try:
       idade = int(input('Idade: '))
    except ValueError:
       continue
    if idade > 18:
        contadordeidade += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo == 'M' or sexo == 'F':
           break
        else:
            continue
    if sexo == 'M':
        contadordehomens += 1
    if sexo == 'F':
        contadordemulheres += 1
    contadordepessoas += 1
    print(f'Foram cadastradas {contadordepessoas} pessoa(s)')
    while True:
        escolha = str(input('Continuar? [S/N]: ')).upper()
        if escolha == 'S' or escolha == 'N':
            break
        else:
            continue
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
if contadordeidade == 0:
    print('Não foi cadastrado nenhuma pessoa com mais de 18 anos')
else:
    print(f'Existem cadastrado {contadordeidade} pessoas com mais de 18 anos')
if contadordehomens == 0:
    print(f'Não foi cadastrado nenhum homem')
elif contadordehomens == 1:
    print(f'Foi cadastrado {contadordehomens} homem')
else:
    print(f'Foram cadastrados {contadordehomens} homens')
if contadordemulheres == 0:
    print('Não foi cadastrado nenhuma mulher')
elif contadordemulheres > 1:
    print(f'Foram cadastradas {contadordemulheres} mulheres com menos de 20 anos')
elif contadordemulheres == 1:
    print(f'Foi cadastrado {contadordemulheres} mulher com menos de 20 anos')
print('Fim, volte sempre!')
