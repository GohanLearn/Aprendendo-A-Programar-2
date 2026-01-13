# Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

# Definindo valores:
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

# calculando e mostrando:
resultSoma = a + b
print('A soma entre "A" e "B" resulta em: ', resultSoma)
if resultSoma < c:
    print(f'O resultado da soma({resultSoma}) é menor que C({c}).')
elif c == resultSoma:
    print(f'O resultado da soma({resultSoma}) é igual a C({c}).')
else:
    print(f'O resultado da soma({resultSoma}) é maior que C({c}).')