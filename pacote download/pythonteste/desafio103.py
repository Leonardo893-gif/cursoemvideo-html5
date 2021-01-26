def ficha(nome, goals):
    return f"O jogador {'desconhecido' if nome == '' else nome} marcou {gols} goals"


# Programa Principal
name = str(input("What´s your name? "))
gols = str(input("Goals: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
print(ficha(name, gols))
