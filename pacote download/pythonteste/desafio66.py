cont = 0
soma = 0
while True:
    num = int(input('Digite um valor \033[0;32m (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'\033[1;31mVocê informou {cont} números e a soma entre eles é {soma}!')
