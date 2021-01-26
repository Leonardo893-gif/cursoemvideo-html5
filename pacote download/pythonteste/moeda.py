def dobro(numero = 0):
    return numero * 2


def metade(numero = 0):
    return numero / 2


def aumentar(numero = 0):
   porc = numero + (numero * 10 / 100)
   return porc

def diminuir(numero = 0):
    porc = numero - (numero * 13 / 100)
    return porc

def moeda(numero = 0, moeda = 'R$', opc=False):
    if opc == True:
        return f'{moeda}{numero:2.2f}'.replace(',',',')

