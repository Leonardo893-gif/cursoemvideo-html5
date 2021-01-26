def voto(ano_nascimento):
    from datetime import date
    nasc = int(input('Enter your year of birth: '))
    ano = date.today().year
    resul = ano - nasc
    if resul < 18:
        return 'Voto negado'
    elif resul > 65:
        return "Voto opcional"
    elif resul > 17 and resul < 64:
        return "Voto obrigatório"


print(voto(2003))
