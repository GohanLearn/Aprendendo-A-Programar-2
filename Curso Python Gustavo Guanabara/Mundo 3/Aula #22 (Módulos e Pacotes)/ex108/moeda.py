def moeda(val):
    return f'R${val:.2f}'.replace('.', ',')


def aumentar(val, percent):
    return val + ((val / 100) * percent)


def diminuir(val, percent):
    return val - ((val / 100) * percent)


def dobro(val):
    return val * 2


def metade(val):
    return val / 2