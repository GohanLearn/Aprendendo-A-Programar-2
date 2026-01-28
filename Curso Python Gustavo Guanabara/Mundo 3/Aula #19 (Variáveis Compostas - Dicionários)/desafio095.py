# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# DESAFIO 093:

# programa:
jogador = dict()
jogadores = list()
gols = list()
while True:
    print('-'*15)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
        if escolha in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if escolha in 'Nn':
        break
print('-='*30)
print('cod ', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
while True:
    print('-'*40)
    escolha = int(input('Mostrar os dados de qual jogador? '))
    if escolha == 999:
        break
    if escolha < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}')
        for i, g in enumerate(jogadores[escolha]['gols']):
            print(f'    => Na partida {i+1}, fez {g} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente')