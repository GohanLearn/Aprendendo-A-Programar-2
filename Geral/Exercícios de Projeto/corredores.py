def somar(corredorTemp):
    valor = 0
    total = float(0)
    tamanho = len(corredorTemp)
    for valor in range (0, tamanho):
        total += corredorTemp[valor]
    result = total
    return float(result)


numCorredor = 0
corredorTemp = [0]
quantia = int(input("Quantos corredores serão? "))
for numCorredor in  range (1, (quantia + 1)):
    corredorTemp.append(float(input(f"Qual tempo do {numCorredor}º corredor? ")))
    numCorredor = numCorredor + 1
for numCorredor in  range (1, (quantia + 1)):
    print(f"Tempo do corredor {numCorredor}: {corredorTemp[numCorredor]}")
media = float(somar(corredorTemp) / quantia)
print(f"Média de tempo: {media}")