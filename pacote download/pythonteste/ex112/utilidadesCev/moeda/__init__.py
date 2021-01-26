def dobro(numero = 0, opc=False):
    met = numero * 2
    return met if opc is False else moeda(met)


def metade(numero = 0, opc=False):
    met = numero / 2
    return met if opc is False else moeda(met)


def aumentar(numero = 0, opc=False):
   porc = numero + (numero * 10 / 100)
   return porc if opc is False else moeda(porc)


def diminuir(numero = 0, opc=False):
    porc = numero - (numero * 13 / 100)
    return porc if opc is False else moeda(porc)


def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero:2.2f}'.replace(',',',')

def resumo(numero, aum=80, red=35):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado:   \t{moeda(numero)}')
    print(f'Dobro do preço:    \t{dobro(numero, True)}')
    print(f'Metade do preço:   \t{metade(numero, True)}')
    print(f'{aum}% de aumento:    \tR${numero + (numero * 88 / 100):.2f}')
    print(f'{red}% de redução:    \tR${numero - (numero * 35 / 100):.2f}')
    print('-'*30)
