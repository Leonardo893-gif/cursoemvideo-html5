estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['siola'] = str(input('Siola do Estado: '))
    brasil.append(estado.copy()) # Faz a cópia entre a lista e o dicionário, seria o [:] das listas
print(brasil)
for e in brasil: # Aqui mostra o campo uf tem {} tem {} {}
   for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil: # Aqui esta mostrando a Unidade Federativa e a Siola Juntos
    for v in e.values():
        print(v, end=' ')
    print() # print para não pular de linha
