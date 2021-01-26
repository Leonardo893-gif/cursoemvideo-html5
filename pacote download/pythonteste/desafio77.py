nomes = 'PROGRAMAR', 'ESTUDO', 'PYTHON', 'JOGADOR', 'JAVASCRIPT', 'AMOR'
vogais = 'A', 'E' , 'I' , 'O', 'U'
for a in nomes:
    print(f'\nNa palavra {a.upper()} temos ás vogais: \n')
    for v in range(0, len(a)):
        if a[v] in vogais:
            print(a[v])
