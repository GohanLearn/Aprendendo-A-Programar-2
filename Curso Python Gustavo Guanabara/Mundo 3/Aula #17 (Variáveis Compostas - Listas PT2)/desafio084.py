# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# programa:
grupo = list()
pessoas = list()
maiorN = list()
menorN = list()
menor = totpessoa = maior = 0
while True:
    pessoas.clear()
    totpessoa += 1
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    grupo.append(pessoas[:])
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    if escolha in 'Nn':
        break
for p in grupo:
    if menor == 0:
        menor = p[1]
    if p[1] >= maior:
        if p[1] > maior:
            maiorN.clear()
        maiorN.append(p[0])
        maior = p[1]
    if p[1] <= menor:
        if p[1] < menor:
            menorN.clear()
        menorN.append(p[0])
        menor = p[1]
print(f'Ao todo, você cadastrou {totpessoa} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end = '')
for m in maiorN:
    print(m, end = ' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end = '')
for n in menorN:
    print(n, end = ' ')