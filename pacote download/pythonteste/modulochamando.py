import Modulos
l = []
for x in range(10):
    l.append(Modulos.valida_inteiro("Digite um número:", 0, 20))
print(f"Soma: {sum(l)}")
