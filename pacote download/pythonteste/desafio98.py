from time import sleep
def contador(l):
    #Funcões:
    print('-'*l)
def cont(inicio,fim,passo):
    if passo < 0:
        passo = passo* -1
    elif passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim: # Verifica se o inicio é maior que o fim
        passo = passo*-1 # Se for eu faço: passo x -1 (de trás pra frente)
    for a in range(inicio,fim,passo):
        print(a,end=' ')
        sleep(1) # Espera 1 segundo
    print(fim,end='') # Mostra o fim da contagem
    print(' Fim!')
#Resto do programa:
contador(20)
cont(1,10,1) # Está contando de 1 até 10 de 1 em 1
contador(20)
cont(10,0,2) # Está contando de 10 até 0 de 2 em 2
contador(20)
print('Agora é a sua vez de personalizar a contagem!')
resp = int(input('Inicío: '))
e = int(input('Fim: '))
p = int(input('Passo: '))
contador(20)
cont(resp,e,p) # Mostra o resultado que o usuário digitou
print('-'*20)
