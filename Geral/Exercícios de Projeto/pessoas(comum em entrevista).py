listaNumerica = []
listaNum = []
contador = 0
for contador in range(5):
    listaNumerica.append(int(input(f"Digite o valor {contador + 1}:")))
for contador in range(5):
    listaNum.append(listaNumerica[contador])
print(f"ListaA: {listaNumerica} - ListaB: {listaNum}")
