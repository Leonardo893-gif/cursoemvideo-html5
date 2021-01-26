import random
def maior(num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    n = list()
    v = 0
    for c in range(0, num):
        n.append(random.randint(0, 10))
        if v < n[c]:
            v = n[c]
        print(f'{n[c]} ', end=' ')
    print(f'. Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {v}.')


# Programa principal
maior(random.randint(1, 8))
