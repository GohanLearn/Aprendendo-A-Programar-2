# Faça um programa que leia um número qualquer e mostre seu fatorial.

num = int(input('Digite um número: '))
fatorial = 1
print(f'{num}! = ', end = '')
for num in range(num, 0, -1):
    print(num, end = '')
    if num - 1 != 0:
        print(' x ', end = '')
    fatorial *= num
print(f' = {fatorial}')