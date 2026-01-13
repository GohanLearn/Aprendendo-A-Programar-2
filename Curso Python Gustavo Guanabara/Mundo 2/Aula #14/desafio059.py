# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar 
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# programa:

# importando bibliotecas:
import os

# obtendo valores
while True:
    val1 = float(input('Digite o primeiro valor: '))
    val2 = float(input('Digite o segundo valor: '))
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa""")
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        soma = val1 + val2
        print(f'\033[1;35m{val1} + {val2} = {soma}\033[m')
        input('Pressione ENTER para recomeçar.')
        os.system('cls')
        continue
    elif escolha == 2:
        vezes = val1 * val2
        print(f'\033[1;35m{val1} x {val2} = {vezes}\033[m')
        input('Pressione ENTER para recomeçar.')
        os.system('cls')
        continue
    elif escolha == 3:
        maior = val2 if val1 < val2 else val1
        print(f'\033[1;35mO maior valor é {maior}\033[m')
        input('Pressione ENTER para recomeçar.')
        os.system('cls')
        continue
    elif escolha == 4:
        os.system('cls')
        continue
    elif escolha == 5:
        os.system('cls')
        print('\033[1;31mPrograma encerrado.')
        break
    else:
        print('\033[1;31mOpção inválida.\033[m')