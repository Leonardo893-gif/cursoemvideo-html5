import moeda
num = float(input('Digite um número: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'Aumentando 10% de {moeda.moeda(num)} dá {moeda.moeda(moeda.aumentar(num))}')
print(f'Diminuindo 13% de {moeda.moeda(num)} dá {moeda.moeda(moeda.diminuir(num))}')
