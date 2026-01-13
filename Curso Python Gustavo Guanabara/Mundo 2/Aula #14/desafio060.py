# Faça um programa que leia um número qualquer e mostre seu fatorial.

# programa:
num = int(input('Digite um número: '))
cont = num
fatorial = 1
print(f'{num}! =', end = ' ')
while cont > 0:
    fatorial = fatorial * cont
    print(f'{cont}', end = ' ')
    if cont != 1:
        print('x ', end = '')
    cont -= 1
print(f'= {fatorial}')