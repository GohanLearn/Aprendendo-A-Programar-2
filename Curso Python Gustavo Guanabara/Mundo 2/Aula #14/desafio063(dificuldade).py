# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Número de elementos que você quer: '))
cont = 0
elemento1 = 0
elemento2 = 1
while cont < n:
    valor = elemento1
    if cont > 0:
        print(' -> ', end = '')
    print(elemento1, end = '')
    valor = elemento1 + elemento2
    elemento1 = elemento2
    elemento2 = valor
    cont += 1