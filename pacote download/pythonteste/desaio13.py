salario = float(input('Qual é o seu salário atualmente? '))
print('Você vai ter o aumento de 15%')
aumento = salario +(salario * 15 / 100)
print('O funcionário teve um aumento de {:.2f},com 15% de aumento o salário é de {:.2f}'.format(salario, aumento))