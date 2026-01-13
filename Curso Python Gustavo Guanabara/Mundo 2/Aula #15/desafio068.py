# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
print('-=-'*20)
print('\033[1;35mPar ou Ímpar\033[m')
print('-=-'*20)
escolha = str(input('Escolha Par ou Ímpar: ')).capitalize().strip()
while True:
    jogadaC = randint(0, 10)
    jogadaP = int(input('Digite um valor de 0 a 10: '))
    if (jogadaC + jogadaP) % 2 != 0:
        vencedor = 'Ímpar'
    else:
        vencedor = 'Par'
    if vencedor != escolha:
        print(f'Você jogou {jogadaP} e o computador jogou {jogadaC}. Total: {jogadaP+jogadaC} \033[1;31m(Ímpar)\033[m')
        break
    else:
        print(f'Você jogou {jogadaP} e o computador jogou {jogadaC}. Total: {jogadaP+jogadaC} \033[1;32m(Par)\033[m')
        print(f'\033[1;32mVocê venceu!\033[m')
        vitorias += 1
print(f'\033[1;31mVocê perdeu após \033[1;32m{vitorias} vitórias\033[1;31m consecutivas, programa encerrado.\033[m')