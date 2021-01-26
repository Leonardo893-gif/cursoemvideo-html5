def leiaint(num):
    while True:
        try:
            s = int(input(num))
        except:
            print('\033[0:31m Erro! Digite um número inteiro válido\033[m')
            continue

def float(num):
    while True:
        try:
            s = float(input(num))
        except:
            print('\033[0:31m Erro! Digite um número inteiro válido\033[m')
            continue

numero = leiaint('Digite um número real: ')
n = float('Digite um número inteiro: ')
print(f"Você digitou o número real {n} e o número decimal foi {numero}")
