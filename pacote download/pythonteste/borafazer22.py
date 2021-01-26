nome = str(input('Escreva seu nome completo: ')).strip()
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu nome no total tem {} letras'.format(len(nome) - nome.count(' ')))