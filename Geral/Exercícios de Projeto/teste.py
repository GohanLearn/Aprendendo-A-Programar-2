import os
print("____________________________") # exercicio 3

def somar(listaNumerica):
    quantidade = 0
    total = 0
    for listaNumerica in range(0, max):
        total += listaNumerica[quantidade]
        quantidade = quantidade + 1
    return total


listaNumerica = [1]
resultado = 0
quantia = 0
while True:
    if listaNumerica[quantia] == 0:
        os.system('cls')
        listaNumerica.remove[0]
        print("Quantidade: ", quantia)
        print("Total: ", somar(listaNumerica))
        break
    else:
        listaNumerica.append(input("Digite os números desejados a seguir: "))
        quantia = quantia + 1
