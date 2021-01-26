from random import randint
print('='*30)
print('Vamos jogar Par ou Ímpar')
print('='*30)
c = 0
possui = ' '
while True:
    n = int(input('Digite um número: '))
    pc = randint(0, 11)
    s = n + pc
    possui = ' '
    while possui not in 'PI':
        possui = str(input('Ímpar ou Par? [P/I]: ')).upper().strip()[0]
        print(f'Você jogou {n} e o computador {pc}. Total que deu {s}')
        if s %  2 == 0:
            print('Deu PAR!')
        else:
            print('Ímpar')
    if possui == 'P':
        if s % 2 == 0:
            print('Você venceu!')
            c += 1
        else:
            print('Você perdeu!')
            break
    elif possui == 'I':
        if s % 2 == 1:
            print('Você venceu')
            c += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente')
print(f'Game over, o seu número de vitórias foi de {c} vezes')
