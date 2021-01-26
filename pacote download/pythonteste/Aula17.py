num = [2, 5, 9, 1]
nume = num[:] # Cópia dos valores, irá pegar todos os valores de num e jogar em nume
num[2] = 3
num.append(7) # Adiciona um valor
num.sort() # Coloca em ordem crescente
num.sort(reverse=True) # Coloca em ordem decrescente
num.pop() # Remove o último elemento da lista
num.pop(2) # Removeu o valor na posição 2
num.remove(2) # Esta removendo o primeiro valor 2
len() # Lê quantos elementos tem na lista
num.insert(2, 2) # Na posição 2 estou inserindo o valor 2
enumerate # Pega a chave e o valor
if 5 in num: # Verifica se o número 5 esta na lista
    num.remove(5)
else:
    print(f'Não achei o número 5')
print(num)
print(f'Esta lista tem {len(num)} elementos')
