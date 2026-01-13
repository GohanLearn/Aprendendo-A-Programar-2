# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Digite o número de elementos que você quer: '))
valor = 0
elemento = 0 # 1 3
e2 = 1 # 2 5
while n > 0:
    valor = elemento + e2
    print(elemento, end = ' -> ')
    elemento = e2
    e2 = valor
    n -= 1
print('FIM')