from time import sleep
tabuada = int(input('Digite um número qualquer para ver sua tabuada: '))
for t in range(1, 11):
    sleep(2)
    print('{} x {:2} = {}'.format(tabuada, t, tabuada*t))