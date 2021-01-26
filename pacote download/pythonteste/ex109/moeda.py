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

