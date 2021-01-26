nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
conta = nota1 + nota2
soma = conta / 2
if soma < 5.0:
    print('A sua média foi de {}'.format(soma))
    print('Você está REPROVADO!')
elif soma <= 5.0 and 6.9:
    print('A sua média foi de {}'.format(soma))
    print('Você está de RECUPERAÇÃO!')
elif soma >= 7.0:
    print('Parabéns! A sua média é {}'.format(soma))
    print('APROVADO!')