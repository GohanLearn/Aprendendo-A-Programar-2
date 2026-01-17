# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# importando bibliotecas:
from random import randint
from time import sleep

# variáveis:
jogadas = list()
palpites = list()

# programa principal:
print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=- SORTEANDO {jogos} JOGOS -=-=-=-')
for s in range(0, jogos):
    sleep(1)
    palpites.append(randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
    for a in palpites:
        if palpites.count(a) > 1:
            palpites.insert(a, randint(1, 60))
            palpites.pop(a)