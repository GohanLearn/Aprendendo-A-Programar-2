# Nessa aula aprendemos a tratar erros e o que são exceções.

try:
    num = float(input('Numerador: '))
    den = float(input('Denominador: '))
    result = num / den
except Exception as erro:
    print(f'\033[31mERRO! Divisão inválida.\033[m\nProblema encontrado: {erro.__class__}')
else:
    print(result)
finally:
    print('\033[34mVolte sempre!\033[m')