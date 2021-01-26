lanche = 'Hambúrger', 'Suco', 'Pizza', 'Pudim'

for comida in lanche:
    print(f'Eu vou comer {comida}')

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
