jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantas gols ele fez na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Continuar? [S/N]: ')).upper()[0].strip()
        if resp in 'SN':
            break
        print("Erro! Responda com S ou N")
    if resp == 'N':
        break
print('-'*30)
print("cód", end='') # até a linha 22 estou lendo os dados
for i in jogador.keys(): # agora em diante estou mostrando os resultados
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o número {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i}, {time[busca]["nome"]} fez {g} gols.')
    print("-="*40)
print("Volte sempre!")
