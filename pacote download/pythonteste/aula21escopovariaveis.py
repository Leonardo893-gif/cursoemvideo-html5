#def teste():
    #x = 8
   # print(f'Na função teste, n vale {n}')
   # print(f'Na função teste, x vale {x}')

# Programa Principal
#n = 2
#print(f'No programa principal, n vale {n}')
#teste()
#print(f'No programa principal, x vale {x}') # Dá erro porque a variável x é uma variável Local e não Global

def funcao():
    n1 = 4 # Mesmo sendo o mesmo nome da variável global ele funciona
    print(f'N1 dentro vale {n1}') # Dentro quer dizer Variável Global 

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
