# Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto.

# obtendo preço
valor = float(input('Digite o preço do produto: R$'))

# calculando
# valorDesconto = valor / 100 * 5
# resultado = valor - valorDesconto
novo = valor - (valor * 5 / 100)

# mostrando resultado
print('O preço após o desconto de 5% é de R${:.2f}'.format(novo))