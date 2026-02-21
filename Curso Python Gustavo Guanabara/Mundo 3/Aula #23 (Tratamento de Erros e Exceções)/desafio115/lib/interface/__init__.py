def leiaInt(val):
    while True:
        try:
            num = int(input(f'{val}'))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[36m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc