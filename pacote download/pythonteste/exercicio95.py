dados_jogador = {}
dadosdoJogador = []
gols = []
while True:
    dados_jogador.clear()
    gols.clear()
    nome = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols {nome} fez na partida {c+1}? ')))
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if resp != 'S' and resp != 'N':
            continue
        else:
            dados_jogador['nome'] = nome
            dados_jogador['Gols'] = gols[:]
            dados_jogador['Total_partidas'] = partidas
            dados_jogador['Gols_total'] = sum(gols)
            dadosdoJogador.append(dados_jogador.copy())
            break
    if resp == 'S':
        continue
    else:
        break
print('-='*30)
print('CÓD     NOME     GOLS      TOTAL')
print('-='*30)
for j in range(len(dadosdoJogador)):
    print(f'{j:<4}{dadosdoJogador[j]["nome"]:8}{dadosdoJogador[j]["Gols"]!s:<15s}{dadosdoJogador[j]["Gols_total"]!s:<18s}')
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 interromope): '))
    if dados == 999:
        print('Volte sempre!')
        break
    elif dados >= len(dadosdoJogador):
        print(f'Não existe jogador com o número {dados}! Tente novamente!')
        continue
    print(f'Levantamento do jogador {dadosdoJogador[dados]["nome"]}')
    for d in range(len(dadosdoJogador[dados]["Gols"])):
        print(f'No jogo {d}, {dadosdoJogador[dados]["nome"]} marcou {dadosdoJogador[dados]["Gols"][d]} gols')
