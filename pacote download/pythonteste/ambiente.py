try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Sempre o finalyy é executado!')

