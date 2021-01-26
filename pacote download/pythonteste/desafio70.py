from time import sleep
print('Welcome!')
print('-'*30)
print('Loja Aonde o seu dinheiro vale mais!')
print('-'*30)
soma = 0
produtoscustammaisde1000 = 0
contador = 0
menor = 0
barato = ""
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço do Produto: R$'))
    soma = soma + preço
    contador = contador + 1
    if preço > 1000:
        produtoscustammaisde1000 = produtoscustammaisde1000 + 1
    if contador == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Continuar? S/N ')).upper().strip()
    if resposta == "N":
        break
print('Analisando a sua compra...')
sleep(2)
print(f'O total da compra é R${soma:2.2f}')
print(f'{produtoscustammaisde1000} produto(s) custam mais de R$1000 reais')
print(f'O Produto mais barato é {barato} e custa R${menor:2.2f}')
print('-'*30)
