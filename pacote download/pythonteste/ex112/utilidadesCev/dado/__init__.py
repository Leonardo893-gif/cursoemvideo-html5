def leiaDinheiro(msg): # leiadinheiro -> Nome da minha Função e msg está passando como parametro
   valido = False # O válido começa a ser Falso
   while not valido: # Enquanto não for válido eu faço:
       entrada = str(input(msg)).replace(',','.').strip() # Está passando o parametro msg como input e o replace está substituindo todas as vírgulas por ponto -> .
       if entrada.isalpha() or entrada.strip() == '': # Verifica se a entrada é alfanúmerica ou se a entrada for igual a '' se o usuário não digitar nada
           print(f'\033[0;31mOPS! \"{entrada}\" não é um número!\033[m') # Imprime a msg
       else: # Se não
           valido = True # O válido passa a ser verdadeiro
           return float(entrada) # Retorna o float da entrada
