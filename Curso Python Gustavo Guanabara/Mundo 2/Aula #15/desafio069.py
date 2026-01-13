# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

# programa:
maiores = homens = mulheresMenores = 0
while True:
    print('-'*30)
    print('    CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheresMenores += 1
    print('-'*30)
    escolha = str(input('Quer continuar? [S/N] '))
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] '))
    if escolha in 'Nn':
        break
print(f'{maiores} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheresMenores} mulheres tem menos de 20 anos.')