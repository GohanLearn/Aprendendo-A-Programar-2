while True:
    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))
    analise(num1, num2)
    operacao = (input("What's the operation? "))
    break


# operação:
if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "/":
    result = num1 / num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "%":
    result = num1 % num2
else:
    print("Please digit a valid operation (+-%*/)")