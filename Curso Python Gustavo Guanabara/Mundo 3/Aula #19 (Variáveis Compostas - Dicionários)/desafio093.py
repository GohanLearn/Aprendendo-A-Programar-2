# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feito durante o campeonato.

# programa:
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
jogador['gols'] = gols
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['total'] = sum(gols)
print('-=-'*15)
print(jogador)
print('-=-'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=-'*15)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for i, g in enumerate(gols):
    print(f'    => Na partida {i}, fez {g} gols.') 
print(f'Foi um total de {jogador['total']} gols.')