# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3.
# C) Quais foram os números pares.

# variáveis globais:
noves = 0
position = 0

# programa
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
valor3 = int(input('Digite mais um número: '))
valor4 = int(input('Digite o último número: '))

# definindo
valores = (valor1, valor2, valor3, valor4)
for c, i in enumerate(valores):
    if i == 9:
        noves += 1
    if i == 3 and position == 0:
        position = c + 1

# mostrando
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {noves} vezes.')
if position != 0:
    print(f'O valor 3 apareceu na {position}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares foram: ', end = '')
for i in valores:
    if i % 2 == 0:
        print(i, end = ' ')