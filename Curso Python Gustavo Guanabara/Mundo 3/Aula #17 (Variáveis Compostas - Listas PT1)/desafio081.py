# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# programa:
numeros = []
escolha = 'S'
while escolha in 'Ss':
    numeros.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
print(f'Ao todo, foram digitados {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'A lista ordenada em ordem decrescente: {numeros}')
if 5 in numeros:
    print(f'O número 5 está na posição {numeros.index(5)} e está na lista!')
else:
    print('O número 5 não está na lista.')