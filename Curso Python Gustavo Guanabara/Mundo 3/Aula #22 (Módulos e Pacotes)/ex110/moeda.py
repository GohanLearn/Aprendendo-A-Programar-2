def moeda(val):
    return f'R${val:.2f}'.replace('.', ',')


def aumentar(val, percent, formata=False):
    if formata:
        return moeda(val + ((val / 100) * percent))
    else:
        return val + ((val / 100) * percent)


def diminuir(val, percent, formata=False):
    if formata:
        return moeda(val - ((val / 100) * percent))
    else:
        return val - ((val / 100) * percent)


def dobro(val, formata=False):
    if formata:
        return moeda(val * 2)
    else:
        return val * 2


def metade(val, formata=False):
    if formata:
        return moeda(val / 2)
    else:
        return val / 2


def resumo(val, aumento, redução):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(val)}')
    print(f'Dobro do preço: \t{dobro(val, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(val, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(val, redução, True)}')
    print('-'*30)