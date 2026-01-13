print('Registro de vendas no Posto Panda: ')
numTipos = 3
listaVenda = []
for i in range(numTipos):
    litros = float(input(f'Quantidade de litros vendida do combustível {i + 1}: '))
    listaVenda.append(f'Tipo {i + 1}: Qtde litros: {litros:.2f}')
for j in range(numTipos):
    print(listaVenda[j])