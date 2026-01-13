# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# obtendo salário
salario = float(input('Informe o salário: R$'))

# checando e calculando
if salario > 1250:
    aumento = (salario / 100) * 10
else:
    aumento = (salario / 100) * 15
novo = aumento + salario
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.')