# Crie um programa que faça o programa jogar Jokenpô com você.

# importando bibliotecas
from random import randint
from time import sleep
import os

# listas:
itens = ('Pedra', 'Papel', 'Tesoura')

# jogando
while True:
    os.system('cls')
    print('\033[1;33mVamos jogar Jokenpô? Suas opções:\033[m')
    print('0 - Pedra\n1 - Papel\n2 - Tesoura\n')
    usuario = int(input('Escolha uma opção: '))
    if usuario != 0 and usuario != 1 and usuario != 2:
        print('Opção inválida!')
        input('Pressione ENTER para recomeçar o jogo. ')
        continue
    computador = randint(0, 2)

# pausa dramática
    os.system('cls')
    sleep(1)
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Pô!')
    sleep(0.5)
    print('\n')

# analisando
    print('-=-'*11)
    print(f'Computador jogou {itens[computador]}.')
    print(f'Jogador jogou {itens[usuario]}.')
    print('-=-'*11)
    if computador == 0:
        if usuario == 0:
            print('\033[1;33mEmpate!\033[m')
        elif usuario == 1:
            print('\033[1;32mO usuário venceu.')
        elif usuario == 2:
            print('\033[1;31mO usuário perdeu.')
    elif computador == 1:
        if usuario == 0:
            print('\033[1;31mO usuário perdeu.')
        elif usuario == 1:
            print('\033[1;33mEmpate!\033[m')
        elif usuario == 2:
            print('\033[1;32mO usuário venceu.')
    elif computador == 2:
        if usuario == 0:
            print('\033[1;31mO usuário venceu.')
        elif usuario == 1:
            print('\033[1;31mO usuário perdeu.')
        elif usuario == 2:
            print('\033[1;33mEmpate!\033[m')
    input('Pressione ENTER para recomeçar o jogo. ')
    os.system('cls')
    continue