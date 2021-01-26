dadosdoJogador = {}
dadosdoJogadorlist = []
golsunit = []
while True:
    dadosdoJogador.clear()
    golsunit.clear()
    print('='*40)
    nome = input('Nome do Jogador: ')
    total = int(input(f'Quantidade de partidas que {nome} jogou: '))
    for c in range(total):
        golsunit.append(int(input(f'Quantos gols {nome} fez na partida {c}?  ')))
    while True:
        escolha = input('Deseja continuar? [S/N]: ').upper()
        if escolha != 'S' and escolha != 'N':
            continue
        else:
            dadosdoJogador["nome"] = nome
            dadosdoJogador["totaldepartidas"] = total
            dadosdoJogador["gols"] = golsunit[:]
            dadosdoJogador["golstotal"] = sum(golsunit)
            dadosdoJogadorlist.append(dadosdoJogador.copy())
            break
    if escolha == 'S':
        continue
    else:
        break
print('-='*30)
print(f'{"Nº":<2}{"Nome":>6}{"Gols":>10}{"Total":>12}')
print('-'*50)
for p in range(len(dadosdoJogadorlist)):
    print(f'{p:<4}{dadosdoJogadorlist[p]["nome"]:8}{dadosdoJogadorlist[p]["gols"]!s:<15s}{dadosdoJogadorlist[p]["golstotal"]!s:<18s}')
while True:
    showinfo = int(input('Mostrar dados de qual jogador (999 interrompe): '))
    if showinfo == 999:
        print('Volte sempre!')
        break
    elif showinfo >= len(dadosdoJogadorlist):
        print(f'Erro! Não existe jogador com o número {showinfo}! Tente novamente!')
        continue
    print(f' --- Levantamento do jogador {dadosdoJogadorlist[showinfo]["nome"]}')
    for c in range(len(dadosdoJogadorlist[showinfo]["gols"])):
        print(f'No jogo {c} fez {dadosdoJogadorlist[showinfo]["gols"][c]}')
