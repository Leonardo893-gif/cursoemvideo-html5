parênteses = list()
parênteses.append(str(input('Digite uma expressão: ')))
for p in parênteses:
    a = p.count('(')
    b = p.count(')')
    if a == b:
        print('Expressão Correta!')
    elif a != b:
        print('Expressão Incorreta!')
