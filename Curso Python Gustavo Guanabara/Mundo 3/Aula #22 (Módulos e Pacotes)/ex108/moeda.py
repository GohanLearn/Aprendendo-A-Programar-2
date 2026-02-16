def moeda(val=0):
    return f'R${val:.2f}'.replace('.', ',')


def aumentar(val=0, percent=0):
    return val + ((val / 100) * percent)


def diminuir(val=0, percent=0):
    return val - ((val / 100) * percent)


def dobro(val=0):
    return val * 2


def metade(val=0):
    return val / 2