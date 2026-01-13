# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

# programa:
num = int(input('Digite um número: '))
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
        print(f'\033[1;33m{i}\033[m', end = ' ')
    else:
        print(f'\033[1;31m{i}\033[m', end = ' ')
if divisores == 2:
    print()
    print(f'O número {num} é primo pois só foi divisível por 1 e por ele mesmo.')
else:
    print()
    print(f'O número {num} foi divisível {divisores} vezes, e por isso não é primo.')