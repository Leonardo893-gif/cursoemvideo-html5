sexo = str(input('Informe seu sexo: [F/M]')).upper().strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos, tente novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
