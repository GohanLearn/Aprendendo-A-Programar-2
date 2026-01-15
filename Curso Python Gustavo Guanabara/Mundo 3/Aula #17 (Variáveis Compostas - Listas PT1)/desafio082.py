# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

# programa:
numeros = []
escolha = 'S'
while escolha in 'Ss':
    numeros.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar? [S/N] ')).strip()[0]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista de números: {numeros}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')