# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

# programa:

# definindo preço e forma de pagamento
valor = float(input('Digite o preço do produto: R$'))
print('\n', '-=-'*20)
print('= Formas de Pagamento =\n1 - Dinheiro/Cheque\n2 - Cartão')
print('-=-'*20, '\n')
pagamento = int(input('Escolha a forma de pagamento: '))

# calculando e respondendo
if pagamento == 1:
    total = valor - (valor / 100 * 10)
elif pagamento == 2:
    parcelas = int(input('Digite em quantas vezes quer parcelar (Digite 1 se não quiser): '))
    if parcelas == 1:
        total = valor - (valor / 100 * 5)
    elif parcelas == 2:
        total = valor
    else:
        total = valor + (valor / 100 * 20)
print(f'O total a pagar é de \033[1;33mR${total:.2f}\033[m') # resposta