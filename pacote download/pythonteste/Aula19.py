dados = {'nome': 'Pedro','idade': 25}
dados['sexo']= 'M' # Adiciona um elemento no dicionário
print(dados)
del dados['idade'] # Remove o elemento do dicionário
filme = {'titulo':'Star Wars','ano': 1997 ,'diretor':'George Lucas' }
print(filme.values()) # Pega todos os valores
print(filme.keys()) # Pega a parte de baixo: titulo, ano e diretor
print(filme.items()) # Pega todos os itens

for k, v in filme.items(): # O For faz uma volta
    print(f'O {k} é {v}')

pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'siola': 'RJ'}
estado2 = {'uf': 'São Paulo', 'siola': 'SP'}
brasil.append(estado1) # Adiciona o estado1 na lista brasil
brasil.append(estado2) #Adiciona o estado2 na lista brasil
print(estado1, estado2)
print(brasil[0]) # Mostra o estado que foi adicionado primeiro
print(brasil[1]) # Mostra o 2° estado
print(brasil[0]['uf']) # Mostra a UF do Ìndice 0
print(brasil[1]['siola']) # Mostra a Siola do Índice 1
