primeiro = int(input('Qual é o primeiro termo da PA: '))
razão = int(input('Qual é a razão: '))
decimo = primeiro + (10 - 1) * razão
for dez in range(primeiro, decimo + razão, razão):
    print('{}'.format(dez), end='-> ')
print('Estes são os 10 Primeiros termos da PA')