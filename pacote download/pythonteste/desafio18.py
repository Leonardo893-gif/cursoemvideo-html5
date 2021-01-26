import math
ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O seno do Ângulo {} é de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O Cosseno do Ângulo {} é de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('A Tangente do Ângulo {} é de {:.2f}'.format(ângulo, tangente))