# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as defstrings da função.


# funções:
def notas(* nota, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    ficha = dict()
    ficha['total'] = len(nota)
    ficha['maior'] = max(nota)
    ficha['menor'] = min(nota)
    ficha['média'] = sum(nota)/len(nota)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        elif ficha['média'] >= 5:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'
    return(ficha)


# programa principal:
resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)