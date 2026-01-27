# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleátorios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# bibliotecas
from random import randint
from time import sleep
from operator import itemgetter

# programa
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # importante
print('Ranking dos jogadores:')
for c, n in enumerate(ranking, start=1):
    print(f'    {c}º lugar: {n[0]} com {n[1]}')
    sleep(1)