def par_impar(n=0):
    if n % 2 == 0:
        return "É par"
    else:
        return False


num = int(input('Número: '))
print(par_impar(num))
if par_impar(num):
    print('É par!')
else:
    print('Não é par!')
