# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade de digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# funções:

def leiaInt(val):
    while True:
        try:
            num = int(input(f'{val}'))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return num


def leiaFloat(val):
    while True:
        try:
            num = float(input(f'{val}'))
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            return num


# programa principal:

inteiro = leiaInt('Digite um Inteiro: ')
real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')