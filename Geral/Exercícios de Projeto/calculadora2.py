# imports
import os

# funções
def operar(num1, num2, operador):
    if operador == "+":
        resultado = num1 + num2
        return resultado
    elif operador == "-":
        resultado =  num1 - num2
        return resultado
    elif operador == "/":
        resultado =  num1 / num2
        return resultado
    elif operador == "%":
        resultado =  num1 % num2
        return resultado
    elif operador == "*":
        resultado =  num1 * num2
        return resultado
    else:
        return ("Por favor digite apenas operações válidas.")

# calculadora
while True:
    os.system('cls')
    print("Comandos: ")
    print("/op - Mostra as operações disponíveis.")
    print("/sa - Fecha o programa.")
    try:
        num1 = (input("Digite o primeiro número: "))
        if num1 == "/sa":
            os.system('cls')
            print("Programa encerrado pelo usuário.")
            exit()
        elif num1 == "/op":
            print("Operações: + - % * /")
            print(input("Pressione 'Enter' para prosseguir. "))
            continue
        else:
            num1 = float(num1)
        num2 = (input("Digite o segundo número: "))
        if num2 == "/sa":
            os.system('cls')
            print("Programa encerrado pelo usuário.")
            exit()
        elif num2 == "/op":
            print("Operações: + - % * /")
            print(input("Pressione 'Enter' para prosseguir. "))
            continue
        else:
            num2 = float(num2)
        operador = (input("Digite a operação: "))
        print(operar(num1, num2, operador))
        print(input("Pressione 'Enter' para prosseguir. "))
    except ZeroDivisionError:
        print("Divisão impossível.")
        print(input("Pressione 'Enter' para prosseguir. "))
        continue
    except ValueError:
        print("Por favor digite apenas números, operações ou comandos.")
        print(input("Pressione 'Enter' para prosseguir. "))
        continue