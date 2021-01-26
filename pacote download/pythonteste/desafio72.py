num = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', \
      'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', \
      'Catorze', 'Quinze', 'Dessezeis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
      numero = int(input('Digite um número entre 0 e 20: '))
      if numero < 0 or numero > 20:
            print('Tente novamente, Informe um valor válido!')
      else:
             print(f'Você digitou o número {num[numero]}')
      resposta = str(input('Continuar? ')).strip().upper()[0]
      if resposta == 'S':
            continue
      elif resposta == 'N':
            break
print('\033[1;34mVocê saiu do programa!')
