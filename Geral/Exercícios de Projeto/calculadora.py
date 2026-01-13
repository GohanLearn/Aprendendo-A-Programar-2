# imports:
import os

# funções:

def operador(operacao, num1, num2):
    if operacao == "+":
        result = num1 + num2
        return result
    elif operacao == "-":
        result = num1 - num2
        return result
    elif operacao == "/":
        result = num1 / num2
        return result
    elif operacao == "*":
        result = num1 * num2
        return result
    elif operacao == "%":
        result = num1 % num2
        return result
    else:
        print("Please digit a valid operation (+-%*/)")
        return()

# mantendo ordem:
while True:
    print("Digit 'stop' for end the program.")
    num1 = (input("What's the first number? "))
    if num1 == "stop":
        print("Program has been finished by the user.")
        exit()
    else:
        num2 = (input("What's the second number? "))
    if num2 == "stop":
        print("Program has been finished by the user.")
        exit()
    else:
        operacao = (input("What's the operation? "))
    if operacao == "stop":
        print("Program has been finished by the user.")
        exit()
    elif operacao == "/" and num2 == ("0"):
        print("Invalid division.")
    else:
        if num1.isdigit():
            if num2.isdigit():
                num1 = float(num1)
                num2 = float(num2)
                os.system('cls')
                operador(operacao, num1, num2)
                resultado = operador(operacao, num1, num2)
                print("Resultado: ", resultado)
            else:
                os.system('cls')
                print("Please digit just valid numbers.")
        else:
            os.system('cls')
            print("Please digit just valid numbers.")