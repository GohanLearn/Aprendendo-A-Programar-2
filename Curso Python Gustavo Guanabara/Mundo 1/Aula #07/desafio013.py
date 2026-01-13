# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

# obtendo salario
salario = float(input('Digite o salário do funcionário: '))

# calculando
salarioAumento = salario / 100 * 15
resultado = salario + salarioAumento

# mostrando
print('O salário após o aumento é de R${}'.format(resultado))