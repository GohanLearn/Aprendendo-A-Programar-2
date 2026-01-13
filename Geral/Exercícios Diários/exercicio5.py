# Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

# variáveis globais:
salarioMin = 1293.20

# recebendo dados:
salario = float(input('Digite seu salário: '))

# analisando e respondendo:
resultado = salario / salarioMin
print(f'Você recebe {resultado} salário(s) mínimo(s).')