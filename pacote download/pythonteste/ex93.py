gols = []
nome = str(input('Nome do jogador: ')).strip()
print('Welcome!')
while True:
    try:
        partidas = int(input(f'Número de partidas que {nome} jogou: '))
    except ValueError:
        continue
    else:
        break
for c in range(partidas):
    gols.append(int(input(f'Quantos gols {nome} fez na partida {c+1}? ')))
dados = {
        'Nome': nome,
        'Gols': gols,
        'Total': sum(gols)
            }
print('=-'*30)
print(f'nome: {nome}, gols: {gols}, total: {dados["Total"]}')
print(f'O campo nome tem o valor {nome}')
print(f'O campo partidas tem o valor {partidas}')
print(f'O campo gols tem o valor {gols}')
print(f'O campo total tem o valor {dados["Total"]}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas')
print('-='*30)
for c in range(len(dados["Gols"])):
    print(f'Na partida {c+1}, {nome} fez {dados["Gols"][c]} gols')
print(f'No total ele fez {dados["Total"]} gols')
