import time
def linha(l):
    print("-="*l)
def contador(a,b,c):
    if c < 0:
        c = c * -1
    elif c == 0:
        c = 1
    print(f'Contando de {a} até {b} ao passo de {c} em {c}')
    if a > b:
        c = c*-1
    for k in range(a,b,c):
        print(k,end=' ')
        time.sleep(0.25)
    print(b,end=' ')
    print('FIM!')

#Programa principal:
linha(20)
contador(1,10,1)
linha(20)
contador(10,0,2)
linha(20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início:'))
f = int(input('Final:'))
p = int(input('Passo:'))
linha(20)
contador(i,f,p)
