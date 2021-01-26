peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('\033[0;34mPARABÉNS, Você está no PESO IDEAL')
elif 25 <= imc < 30:
    print('Você está no SOBREPESO')
elif 30 <= imc < 40:
    print('\033[0;31mAtenção!Você está na OBESIDADE')
else:
    print('\033[0;31mVocê está na OBESIDADE MÓRBIDA, Cuidado!')
