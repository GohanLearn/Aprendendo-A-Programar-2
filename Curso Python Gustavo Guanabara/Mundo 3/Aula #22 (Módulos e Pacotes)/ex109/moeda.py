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