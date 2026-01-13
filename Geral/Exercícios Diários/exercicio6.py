# Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

# recebendo dado:
valor = float(input('Digite o valor: '))

#reajustando:
reajusteAcres = valor + ((valor / 100) * 5)
reajusteDes = valor - ((valor / 100) * 5)
print(f' O valor com reajuste de 5% de acréscimo é: {reajusteDes}')
print(f' O valor com reajuste de 5% de desconto é: {reajusteAcres}')