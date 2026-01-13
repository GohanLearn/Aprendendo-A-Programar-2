# Faça um programa que leia um número qualquer e mostre seu fatorial.

# programa:
num =  int(input('Digite um número: '))
cont = 0
fatorial = 1
print(f'{num}! = ', end = '')
while cont < num:
    fatorial = fatorial * (num - cont)
    print(f'{num - cont}', end = '')
    if (cont + 1) != num:
        print(' x ', end = '')
    cont += 1
print(' =', fatorial)