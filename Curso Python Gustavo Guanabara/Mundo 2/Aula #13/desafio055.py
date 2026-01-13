# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e qual foi o menor peso lidos.

# lendo:
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa: '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}Kg e o menor foi {menor}Kg.')