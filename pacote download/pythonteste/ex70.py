from time import sleep
print('-'*30)
print('Olá, Seja bem vindo a nossa loja')
print('-'*30)
print('Aonde o seu dinheiro vale mais')
print('-'*30)
cont_15 = soma = cont = menor = 0
barato = ""
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Preço R$: '))
    soma = soma + preço
    cont += 1
    if preço > 1000:
        cont_15 += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = str(input('Continuar: [S/N] ')).upper()
    if resp == 'N':
        break
    continue
print('Analisando a sua compra...')
sleep(3)
print('\033[1;Total da sua compra é de R${:.2f}'.format(soma))
print('{} produtos custam mais de R$1000 reais'.format(cont_15))
print(f'{barato} é o produto mais barato')
