# Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.

# lendo e definindo valores:
a = int(input('Digite o valor A: '))
b = int(input('Digite o valor B: '))

# analisando e mostrando:
if a == b:
    c = a + b
else:
    c = a * b
print(f'O resultado é: {c}')

# obs: fiz as variáveis com letras em minúsculo, pois isso é uma boa conduta na programação.