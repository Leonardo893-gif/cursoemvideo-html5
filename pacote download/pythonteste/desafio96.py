def área():
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento: '))
    total = largura * comprimento
    print(f'Largura: {largura}')
    print(f'Comprimento: {comprimento}')
    print(f'A área de um terreno de {largura} x {comprimento} é de: {total}m².')

área()
