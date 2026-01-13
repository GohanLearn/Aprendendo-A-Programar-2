# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

# programa:
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

# analisando e respondendo
if valor1 > valor2:
    print('O \033[1;36mprimeiro valor\033[m é maior.')
elif valor2 > valor1:
    print('O \033[1;36msegundo valor\033[m é maior')
elif valor1 == valor2:
    print('\033[1;33mNão existe\033[m valor maior, os dois são \033[1;35miguais\033[m.')
else:
    print('\033[31mInválido.')