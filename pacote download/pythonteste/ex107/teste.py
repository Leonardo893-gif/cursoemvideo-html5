import moeda
num = float(input('Digite um número: R$'))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando 10% de {num} dá {moeda.aumentar(num)}')
print(f'Diminuindo 13% de {num} dá {moeda.diminuir(num)}')
