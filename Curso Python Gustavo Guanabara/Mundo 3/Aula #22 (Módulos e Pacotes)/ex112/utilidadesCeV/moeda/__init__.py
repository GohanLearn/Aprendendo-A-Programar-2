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
    print(f'Preço analisado: {moeda(val):>5}')
    print(f'Dobro do preço: {dobro(val, True):>5}')
    print(f'{aumento}% de aumento: {aumentar(val, aumento, True):>5}')
    print(f'{redução}% de redução: {diminuir(val, redução, True):>5}')
    print('-'*30)