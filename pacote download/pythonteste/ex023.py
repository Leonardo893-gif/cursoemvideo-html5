num = int(input('Digite um número: '))
unidade = num // 1 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
milhar = num // 1000 % 10
print('A unidade vale {}'.format(unidade))
print('A centena vale {}'.format(centena))
print('A dezena vale {}'.format(dezena))
print('O Milhar vale {}'.format(milhar))