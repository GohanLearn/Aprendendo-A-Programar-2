def leiaDinheiro(dados):
    válido = False
    while not válido:
        valor = str(input(f'{dados}')).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO: \"{valor}\" é um preço inválido!\033[m')
        else:
            válido = True
    return float(valor)