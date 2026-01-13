# Crie um programa que leia um número inteiro qualquer e mostre na tela se é PAR ou ÍMPAR.

# recebendo número
num = int(input('\033[1;34mDigite um número: \033[33m'))

# respondendo
if (num%2) == 0:
    print(f'\033[1;32mO número \033[1;33{num}\033[1;32;37m é par.')
else:
    print(f'O número {num} é ímpar.')