def notas(* núm, sit=False):
    """
    :param núm: Vários notas
    :param sit: (Opcional) -> Exibe a situação ou não.
    :valor: Dicionário com várias informações
    :tot: Faz a soma e a divisão
    """
    tot = sum(núm) / len(núm)
    if tot >= 7 and sit == True:
        valor = {f'Tamanho: {len(núm)}', f'Maior nota: {max(núm)}', f'Menor nota: {min(núm)}', f'Média da turma: {sum(núm) / len(núm)}', 'Situação: Ótima'}
        print(valor)
    elif tot >= 5 and sit == True:
        valor = {f'Tamanho: {len(núm)}',f'Maior nota: {max(núm)}',f'Menor nota: {min(núm)}', f'Média da turma: {sum(núm) / len(núm)}', 'Situação: Razoável'}
        print(valor)
    elif tot < 5 and sit == True:
        valor = {f'Tamanho: {len(núm)}',f'Maior nota: {max(núm)}',f'Menor nota: {min(núm)}',f'Média da turma: {sum(núm) / len(núm)}', 'Situação Ruim'}
        print(valor)
    else:
        valores = {f'Tamanho: {len(núm)}', f'Maior nota {max(núm)}', f'Menor nota {min(núm)}',f'Média da turma: {sum(núm) / len(núm)}'}
        print(valores)


notas(5.5, 2.5, 1.5, sit=True)
help(notas)
