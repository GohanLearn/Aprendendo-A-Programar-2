# obtendo dados
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))
# fazendo matriz
matriz = []

# informar os dados da matriz
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o elemento da posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
# impressão da matriz
for k in range(linhas):
    print(matriz[k])