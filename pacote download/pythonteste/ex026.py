frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes'.format(frase.count('A')+1))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A letra A aparece na ultima posição {}'.format(frase.rfind('A')+1))