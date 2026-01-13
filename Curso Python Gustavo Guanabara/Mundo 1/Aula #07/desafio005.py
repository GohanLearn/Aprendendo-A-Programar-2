# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

# obtendo número
num = int(input('Digite um número inteiro: '))

# calculando e mostrando
# suc = num + 1
# ant = num - 1
# Quando não for reutilizar a soma, evitar criar variáveis para economizar memória
print('O sucessor do número {} é {} e o antecessor é {}'.format(num, (num+1), (num-1)))