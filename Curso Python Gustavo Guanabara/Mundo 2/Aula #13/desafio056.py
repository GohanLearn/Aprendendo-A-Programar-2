# Desenvolva um programa que leie o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

# programa:
somaIdades = 0
maiorIdade = 0
mulheresMenores = 0
maisVelho = ''
for n in range(1, 5):
    print(f'----- PESSOA {n} -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdades += idade
    if sexo == 'M' and idade > maiorIdade:
        maisVelho = nome
        maiorIdade = idade
    if sexo == 'F' and idade < 20:
        mulheresMenores += 1
media = somaIdades / 4
print(f'\033[1;33mA média de idade do grupo é de {media} anos.')
print(f'\033[1;34mO homem mais velho tem {maiorIdade} anos e se chama {maisVelho.capitalize()}.')
print(f'\033[1;31mAo todo são {mulheresMenores} mulheres com menos de 20 anos.')