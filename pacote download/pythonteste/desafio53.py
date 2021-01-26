frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[0;34mTemos um Palíndromo!')
else:
    print('\033[0;31mA frase digitada não é um Palíndromo!')
