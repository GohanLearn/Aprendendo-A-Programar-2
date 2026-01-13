# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# importando bibliotecas
from random import randint

# pensando
num = randint(0, 10)
print('-=-'*20)
print('\033[1;36mPensei em um número entre 0 e 10, tente adivinhar...\033[m')
print('-=-'*20)

# jogando
palpite = 11
quantia = 0
while palpite != num:
    if quantia > 0:
        if palpite > num:
            print(f'\033[1;31mMenos... Tente mais uma vez.\033[m')
        else:
            print(f'\033[1;31mMais... Tente mais uma vez.\033[m')
    palpite = int(input('Digite seu palpite: '))
    quantia +=  1
print(f'\033[1;33mParabéns, você acertou! Eu escolhi o número {num}')
print(f'\033[1;35mForam ao todo {quantia} palpites para você vencer.')