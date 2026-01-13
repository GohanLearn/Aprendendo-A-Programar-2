# Faça um programa que leia um número qualquer e mostre seu fatorial.

# programa:
num =  int(input('Digite um número: '))
fatorial = 1
print(f'{num}! = ', end = '')
while num != 0:
    fatorial = fatorial * num # pode ser simplifiicado: fatorial += num
    print(f'{num}', end = '')
    if (num - 1) != 0:
        print(' x ', end = '')
    num -= 1
print(' =', fatorial)