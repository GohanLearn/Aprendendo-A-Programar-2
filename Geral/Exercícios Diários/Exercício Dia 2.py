print("____________________________") # exercicio 1:

while True:
    numero = (input("Digit a number: "))
    if numero.isdigit():
        numero = int(numero)
        print("Valid number: ", numero)
        break
    else:
        print("Try Again.")

print("____________________________") # exercicio 2:
import os
def somar(listNumber):
    valor = 0
    total = 0
    for valor in range (0,5):
        total += listNumber[valor]
    result = total
    return result


listNumber = []
number = 1
while True:
    for number in range(1, 6):
        numberUser = (input(f"Digit value {number}: "))
        if numberUser.isdigit():
            numberUser = int(numberUser)
            listNumber.append(numberUser)
        else:
            os.system('cls')
            print("Please just digit valid numbers.")
            break
    else:
        print(somar(listNumber))