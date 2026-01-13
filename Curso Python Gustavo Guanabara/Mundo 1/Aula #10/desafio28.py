# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# imports
from random import randint
from time import sleep
import os
# mantendo programa ativo
os.system('cls')
while True:
# pensando
    numero = randint(0, 5) # pensa em um número
    print('-=-'*20)
    print('\033[35mVou pensar em um número entre 0 e 5, tente adivinhar...\033[m')
    print('-=-'*20)

# resposta do usuário
    resposta = int(input('\033[34mEm que número eu pensei? \033[37m')) # jogador tenta adivinhar
    print('\033[mProcessando...')
    sleep(3)

# analisando
    if resposta == numero:
        print(f'\033[32mParabéns, você acertou! Eu escolhi o número {numero}.')
    else:
        print(f'\033[31mVocê errou! Eu escolhi o numero {numero}.')
    input('\033[mPressione ENTER para continuar o jogo.')
    os.system('cls')
    continue