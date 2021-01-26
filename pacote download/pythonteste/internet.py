from socket import gethostbyname, create_connection

# Verifica se esta conectado a internet
def conectadoInternet():

    tentativas = 0
    servidorRemoto = 'www.google.com.br'

    while tentativas < 3:
        if tentativas == 1:
            servidorRemoto = 'www.lds.org'
        elif tentativas == 2:
            servidorRemoto = 'www.msn.com'

        try:
            host = gethostbyname(servidorRemoto)
            s = create_connection((host, 80), 2)
            return True
        except: tentativas += 1

    return False
