# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

# Ex:
# n = leiaInt('Digite um n')


# funções:
def leiaInt(digit):
    while True:
        num = str(input(f'{digit}'))
        if num.isnumeric():
            return num
        else:
            print('\033[31;1mERRO! Digite um número inteiro válido.\033[m')

# programa principal:
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')