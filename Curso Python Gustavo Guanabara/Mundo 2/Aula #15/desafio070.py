# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

# programa:
total = produtosM = barato = 0
print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
print('-'*40)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    escolha = str(input('Quer continuar? [S/N] '))
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] '))
    total += preço
    if preço > 1000:
        produtosM += 1
    if barato == 0:
        maisBarato = produto
        barato = preço
    else:
        if preço < barato:
            maisBarato = produto
            barato = preço
    if escolha in 'Nn':
        break
print('-'*20, 'FIM DO PROGRAMA', '-'*20)
print(f'Total da compra: R${total:.2f}')
print(f'Produtos que custam mais de R$1000.00: {produtosM:.0f}')
print(f'O produto mais barato foi {maisBarato} que custa R${barato:.2f}')