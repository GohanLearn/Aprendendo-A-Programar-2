# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# programa:
num = []
for i in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))
print(f'\nVocê digitou os valores {num}')
maior = max(num)
menor = min(num)
print(f'O maior valor digitado foi {max(num)} nas posições ', end = '')
for a, b in enumerate(num):
    if b == maior:
        print(f'{a}', end = '...')
print(f'\nO menor valor digitado foi {min(num)} nas posições ', end = '')
for c, d in enumerate(num):
    if d == menor:
        print(f'{c}', end = '...')