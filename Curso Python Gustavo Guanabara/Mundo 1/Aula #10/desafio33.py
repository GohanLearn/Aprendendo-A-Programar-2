# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# obtendo números
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

# definindo maior
if num1 > (num2 and num3):
    maior = num1
if num2 > (num1 and num3):
    maior = num2
if num3 > (num1 and num2):
    maior = num3

# definindo menor
if num1 < (num2 and num3):
    menor = num1
if num2 < (num1 and num3):
    menor = num2
if num3 < (num1 and num2):
    menor = num3

# mostrando
print(f'O maior número é o {maior} e o menor é o {menor}')