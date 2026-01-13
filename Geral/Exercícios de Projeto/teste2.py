import os
print("____________________________") # exercicio 3

def somar(listaNumerica):
    quantidade = 0
    total = 0
    for listaNumerica in range(0, quantia):
        total += listaNumerica[quantidade]
        quantidade = quantidade + 1
    return total


listaNumerica = []
resultado = 0
quantia = 0
while True:
        variavel = int(input("Digite os números desejados a seguir: "))
        if variavel == 0:
            os.system('cls')
            print("Quantidade: ", quantia)
            print("Total: ", somar(listaNumerica))
            break
        else:
            listaNumerica.append(variavel)
            quantia = quantia + 1
