def fatorial(num=1, show=False):
    """
    para show: (opcional) -> Mostrar ou não a conta.
    return: O valor do Fatorial de um número n.
    para n: O número a ser calculado.
    """
    if show == True:
        return f"{n} x {n - 1} x {n - 2} x {n - 3} x {n - 4} = {fatorial(5)}"
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# Programa Principal
n = int(input('Number: '))
print(fatorial(5, True))
help(fatorial)
