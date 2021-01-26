dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilometros percorrido? '))
pago = (dias * 60) + (km + 0.15)
print('O total a pagar é de {:.2f}'.format(pago))