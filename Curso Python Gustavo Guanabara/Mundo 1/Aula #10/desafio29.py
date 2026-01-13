# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

# lendo
velocidade = float(input('\033[34mQual a velocidade do carro? \033[m'))

# analisando e respondendo
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'\033[1;33mVocê foi multado em \033[1;31mR$ {multa:.2f}')
#else:
#    print('Você está dentro do limite de velocidade.')
print("\033[32mTenha um bom dia! Dirija com segurança!")