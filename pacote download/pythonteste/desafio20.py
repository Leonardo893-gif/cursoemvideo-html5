import random
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o segundo: '))
n3 = str(input('Digite o terceiro: '))
n4 = str(input('Digite o quarto: '))
lista = [n1, n2, n3, n4]
sorteado = random.shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)
