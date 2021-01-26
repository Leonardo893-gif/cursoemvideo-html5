while True:
    são_carlos = int(input("Qual a altitude da cidade de São Carlos? "))
    if são_carlos == 856:
        print('Acertou')
    else:
        print('Errou!')
        while True:
              sjc = int(input("Qual a altitude da cidade de São José dos Campos? "))
              if sjc == 600:
                  print("Parabéns")
                  break
              else:
                  print("Desculpe! Você errou!")
        