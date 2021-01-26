print('-'*30)
print('Seja Bem vindo!')
print('-'*30)
totaldepessoas = 0
quantidadedehomens = 0
mulherescommenosde20anos = 0
contadordeidade = 0
while True:
    try:
      idade = int(input('Idade: '))
    except ValueError:
      continue
    if idade >= 18:
        contadordeidade += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo == 'M' or sexo == 'F':
           break
        else:
            continue
    if sexo == 'M':
        quantidadedehomens += 1
    if sexo == 'F' and idade < 20:
        mulherescommenosde20anos += 1
    totaldepessoas += 1
    print(f'Pessoa(s) {totaldepessoas} cadastradas')
    while True:
        escolha = str(input('Continuar [S/N] ')).upper().strip()
        if escolha == 'S' or escolha == 'N':
           break
        else:
            continue
    if escolha == 'S':
        continue
    elif escolha == 'N':
        break
print(f'Existe(m) {contadordeidade} pessoa(s) com mais de 18 anos')
print(f'Foram cadastrados {quantidadedehomens} homem(ns)')
print(f'Foram cadastradas {mulherescommenosde20anos} mulher(es) com menos de 20 anos')
print('Fim, volte sempre!')
