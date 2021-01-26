velocidade = float(input('Quantos km você rodou?'))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('\033[31mVocê foi MULTADO! por ultrapassar os 80km, sua multa é de R${:.2f}'.format(multa))
else:
    print('\033[0;34mVocê andou na velocidade permitida\033[m')