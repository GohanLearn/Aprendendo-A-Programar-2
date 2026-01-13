# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
# melhore o programa para converter em quilometros, hectometros, decametros, decimetros, centimetros e milimetros
# obtendo valor
metros = float(input('Digite a quantidade de metros: '))

# convertendo
quilometros = metros * 0.001
hectometros = metros * 0.01
decametros = metros * 0.1
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

# mostrando
print('A medida de {}m corresponde a\n{}km\n{}hm\n{:.1f}dam\n{}dm\n{}cm\n{}mm'.format(metros, quilometros, hectometros, decametros, decimetros, centimetros, milimetros))