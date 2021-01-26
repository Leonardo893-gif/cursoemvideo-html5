from time import sleep
def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os números')
    for val in num:
        print(f'{ val }',end='', flush=True)
        sleep(0.2)
        if cont == 0:
            maior = val
        else:
            if val > maior:
                maior = val
        cont += 1
    print(f' Foram passados {cont} números ao todo')
    print(f'O maior número informado foi {maior}.')

#Programa principal:
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

