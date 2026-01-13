# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
    # Considere US$1,00 = R$3,27

# obtendo valor
reais = float(input('Quanto dinheiro você tem na carteira? R$'))

# calculando
resultado = reais / 3.27

# mostrando
print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, resultado))