# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas pessoas com idade acima da média.

# programa:
individuo = dict()
pessoas = list()
mulheres = list()
idadeAcima = list()
sumIdades = 0
while True:
    individuo['nome'] = str(input('Nome: '))
    individuo['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
    while not individuo['sexo'] in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        individuo['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
    individuo['idade'] = int(input('Idade: '))
    sumIdades += individuo['idade']
    pessoas.append(individuo.copy())
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    while not escolha in 'NnSs':
        print('ERRO! Responda apenas S ou N.')
        escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    if escolha in 'Nn':
        break
media = sumIdades / len(pessoas)
for p in pessoas:
    if p['sexo'] in 'Ff':
        mulheres.append(p['nome'])
    if p['idade'] > media:
        idadeAcima.append(p)
print('-=-'*15)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media} anos.')
print(f'- As mulheres do grupo são ', end = '')
for i in mulheres:
    print(i, end = ' ')
print()
print(f'- Lista das pessoas com idade acima da média:')
for m in idadeAcima:
    print(f'nome = {m['nome']}; sexo = {m['sexo']}; idade = {m['idade']};')
    print()
print('ENCERRADO')