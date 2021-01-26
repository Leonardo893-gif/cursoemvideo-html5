from random import randint
print('-'*30)
print('Par ou Ímpar')
print('-'*30)
c = 0
parimpar = ''
while True:
    num = int(input('Digite um número: '))
    termo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    computador = randint(0, 10)
    s = computador + num
    while termo not in 'PI':
        termo = str(input('Ímpar ou Par? [I/P] ')).upper().strip()[0]
    if s % 2 == 0:
        parimpar = 'Par'
    else:
        parimpar = 'Ímpar'
    print(f'Você escolheu {num} e o computador {computador}, total que é {parimpar}')
    if termo == 'I' and parimpar == 'Ímpar' or termo == 'P' and parimpar == 'Par':
        print('Vamos jogar novamente')
        c += 1
    else:
        break
print(f'Game Over, você venceu {c} vezes seguidas!')
