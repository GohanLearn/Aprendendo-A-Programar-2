# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# programa:
somaI = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o valor número {i}: '))
    if num % 2 == 0:
        somaI += num
        cont += 1
print(f'\033[1;33mA soma de todos os {cont} números pares que você citou resulta em {somaI}')