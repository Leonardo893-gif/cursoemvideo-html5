def leiaDinheiro(msg):
   valido = False
   while not valido:
       entrada = str(input(msg)).replace(',','.').strip()
       if entrada.isalpha() or entrada.strip() == '':
           print(f'OPS! \"{entrada}\" não é um número!')
       else:
           valido = True
           return float(entrada)
