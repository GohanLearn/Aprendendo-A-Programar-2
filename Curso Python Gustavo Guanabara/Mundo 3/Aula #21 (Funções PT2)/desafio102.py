# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial.

# funções:
def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número
    
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fo Fatorial de um número n.
    """
    f = 0
    for c in range(n, f, -1):
        if show:
            if c != n:
                print(f'x {c} ', end = '')
            else:
                print(f'{c} ', end = '')
        f *= c
    print('= ', end = '')
    return f


# programa principal:
print(fatorial(5, show=False))