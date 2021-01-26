frase = str(input('Digite uma frase para ver se ela é um Palíndromo: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A Frase {} é um Palíndromo'.format(frase))
else:
    print('A frase {} Não é um Palíndromo'.format(frase))