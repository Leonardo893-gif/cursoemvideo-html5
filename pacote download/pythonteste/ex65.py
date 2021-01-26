respond = 'S'
soma = 0
quant = 0
media = 0
maior = 0
menor = 0
while respond in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    respond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média entre eles é {}'.format(quant, media))
print('O maior número é {} e o menor é {}'.format(maior, menor))
print('Obrigado!')
