# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

# obtendo distância
distancia = float(input('Qual a distância da viagem? '))

# calculando e respondendo preço
#if distancia <= 200:
#    preco = distancia * 0.50
#else:
#    preco = distancia * 0.45
#print(f'O preço da viagem é de R$ {preco:.2f}')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da viagem é de R$ {preco:.2f}')