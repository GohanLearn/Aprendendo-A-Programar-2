def leiaDinheiro(dados):
    while True:
        valor = str(input(f'{dados}'))
        valor = valor.replace(',', '.')
        if valor.isnumeric() or valor.isdecimal():
            valor = float(valor)
            return valor
        else:
            while not valor.isnumeric() or valor.isdecimal():
                print(f'\033[1;31mERRO: "{valor}" é um preço inválido!\033[m')
                valor = str(input(f'{dados}'))