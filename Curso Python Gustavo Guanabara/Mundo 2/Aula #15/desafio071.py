# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('BANCO CEV'.center(30))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
cedulas50 = cedulas20 = cedulas10 = cedula1 = 0
while valor != 0:
    if valor >= 50:
        cedulas50 += 1
        valor -= 50
    elif valor >= 20 and valor < 50:
        cedulas20 += 1
        valor -= 20
    elif valor >= 10 and valor < 20:
        cedulas10 += 1
        valor -= 10
    elif valor != 0 and valor < 10:
        while valor != 0:
            cedula1 += 1
            valor -= 1
if cedulas50 > 0:
    print(f'Total de {cedulas50} cédulas de R$50')
if cedulas20 > 0:
    print(f'Total de {cedulas20} cédulas de R$20')
if cedulas10 > 0:
    print(f'Total de {cedulas10} cédulas de R$10')
if cedula1 > 0:
    print(f'Total de {cedula1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')