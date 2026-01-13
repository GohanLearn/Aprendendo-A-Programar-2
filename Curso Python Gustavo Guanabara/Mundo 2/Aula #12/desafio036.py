# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# programa:
valor = float(input('\033[1;33mQual o valor da casa? R$\033[m'))
salario = float(input('\033[1;33mQual o seu salário? R$\033[m'))
anos = int(input('\033[1;33mEm quantos anos vai pagar? \033[m'))

# calculando
prestacao = valor / (anos * 12)
if prestacao > (salario / 100 * 30):
    print('\033[1;31mEmpréstimo negado! O valor da prestação mensal excede 30% do salário.')
else:
    print(f'\033[1;33mEmpréstimo aprovado! Você pagará R${prestacao:.2f} por mês durante {anos} anos até completar o valor de R${valor:.2f}')