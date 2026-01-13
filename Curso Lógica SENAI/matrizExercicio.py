# obtendo valores
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

# formando matriz
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o item [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
for i in range(linhas):
    print(matriz[i])