from random import randint
a = randint(1, 8)
b = randint(1, 8)
c = randint(1, 8)
d = randint(1, 8)
e = randint(1, 8)
s = a, b, c, d, e
ordem = sorted(s)
print(f'Os números gerados são {s}')
print(f'\033[2;34mO maior número é {max(ordem)}')
print(f'\033[3;32mO menor número é {min(ordem)}')
