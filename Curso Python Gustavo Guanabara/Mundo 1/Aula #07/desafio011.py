# Faça um programa que leia a largura e a altura da parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

# obtendo largura e altura
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

# calculando e mostrando
area = largura * altura

# mostrando resultado
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('A quantidade de tinta necessária é de {} litros.'.format(area/2))