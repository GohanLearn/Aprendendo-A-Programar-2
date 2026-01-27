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
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    if escolha in 'Nn':
        break
print('-=-'*15)
print(f'{'cod':<4}{'nome':<15}{'gols':<6}{'total':>8}')
print('---'*15)
for k, v in enumerate(jogadores):
    print(f'{k:<4}{v["nome"]:<15}{v["gols"]!s:>6}{v["total"]:>8}')
while True:
    print('---'*15)
    escolha = int(input('Mostrar os dados de qual jogador? '))
    if escolha == 999:
        break
    if escolha < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[escolha]["nome"]}')
        for i, g in enumerate(jogadores[escolha]['gols']):
            print(f'    => Na partida {i}, fez {g} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente')