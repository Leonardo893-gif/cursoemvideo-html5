respon = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while respon in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    respon = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média entre eles é {}'.format(soma, quant))
print('O maior número é {} o menor é {}'.format(maior, menor))
