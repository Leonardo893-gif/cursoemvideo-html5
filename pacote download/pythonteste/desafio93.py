Nome = str(input('Nome do jogador: ')).strip()
while True:
    try:
        quant_partidas = int(input(f'Quantas partidas o {Nome} jogou?'))
    except ValueError:
        continue
    else:
        break
golsUnidade = []
for c in range(quant_partidas):
    golsUnidade.append(int(input(f'Quantas gols ele fez na partida {c}?')))
dados = {
    'Nome': Nome,
    'Gols': golsUnidade,
    'Total': sum(golsUnidade)
}
print('-='*30)
print(f'nome: {Nome}, gols: {golsUnidade}, total: {dados["Total"]}')
print('-='*30)
#for k, v in dados["Nome"], dados["Gols"], dados["Total"]:
    #print(f'O campo {k} tem o valor {v}')
print(f'O campo nome tem o valor {Nome}.')
print(f'O campo gols tem o valor {golsUnidade}.')
print(f'O campo total tem o valor {dados["Total"]}.')
print('-='*30)
print(f'O Jogador {Nome} jogou {quant_partidas} partidas')
for c in range(len(dados["Gols"])):
    print(f'=> Na {c+1}°partida, ele fez {dados["Gols"][c]} gols.')
print(f'No total {Nome} fez {dados["Total"]} gols.')
