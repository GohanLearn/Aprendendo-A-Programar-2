# Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

# Obtendo número:
num = float(input('Digite um número: '))

# Analisando e imprimindo:
if num % 2 == 0:
    parimpar = ('par')
else:
    parimpar = ('ímpar')
if num > 0:
    maismenos = ('positivo')
else:
    maismenos = ('negativo')
print(f'O número é {parimpar} e {maismenos}.')