# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# funções
def área(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')


# programa principal:
print('Controle de Terrenos'.center(20))
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)