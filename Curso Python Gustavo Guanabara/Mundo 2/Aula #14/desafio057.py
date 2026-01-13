# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# programa:
sexo = ''
while not (sexo == 'M' or sexo == 'F'):
    if not sexo == '':
        print('Por favor digite apenas M (masculino) ou F (feminino).')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
print('Fim')