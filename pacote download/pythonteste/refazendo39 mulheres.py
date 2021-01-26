from datetime import date
recente = date.today().year
nascimento = int(input('Digite o ano que você nasceu: '))
gênero = str(input('Você é do sexo masculino ou feminino? '))
saldo = recente - nascimento
calculo = saldo - 18
if gênero == 'masculino' :
    print('Você tem que se apresentar ao exército!')
    print('Faltam {} anos(o) para você se alistar ao exército!'.format(calculo))
    print('LEMBRANDO: Você é OBRIGADO a se apresentar se não terá consequências!')
if gênero == 'feminino':
    print('Não é OBRIGATÓRIO você se apresentar ao exército!')
    print('Você pode se alistar se você quiser!')