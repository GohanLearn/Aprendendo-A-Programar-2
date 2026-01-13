# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# importando bibliotecas
from random import randint

# variáveis globais
menor = 0
maior = 0

# tupla:
listagem = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

# mostrando tupla
for i in listagem:
    print(i, end = ' ')
    if i > maior:
        maior = i
    if i < menor or menor == 0:
        menor = i

# mostrando maior e menor
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')