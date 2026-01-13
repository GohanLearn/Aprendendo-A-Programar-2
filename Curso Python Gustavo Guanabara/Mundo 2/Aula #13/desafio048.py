# Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de de 3 e que se encontram no intervalo de 1 até 500.

# programa:
total = 0
cont = 0
for i in range(0, 500, 3):
    if i % 2 != 0:
        total += i
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {total}')