from datetime import date
ano = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('\033[0;31mNadador MIRIM!')
elif idade <= 14:
    print('\033[7;30mNadador INFANTIL!\033[m')
elif idade <= 19:
    print('\033[0;33mNadador JUNIOR!')
elif idade <= 25:
    print('\033[0;36mNadador SÊNIOR!')
elif idade > 25:
    print('\033[0;35mNadador MASTER!')
