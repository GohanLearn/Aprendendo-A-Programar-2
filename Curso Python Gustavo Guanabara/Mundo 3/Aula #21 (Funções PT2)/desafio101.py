# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

# bibliotecas:
from datetime import date


# funções:
def voto(nasc):
    if nasc >= 18:
        if nasc > 65:
            return f'Com {nasc} anos: VOTO OPCIONAL'
        else:
            return f'Com {nasc} anos: VOTO OBRIGATÓRIO'
    elif nasc < 16:
        return f'Com {nasc} anos: NÃO VOTA'
    else:
        return f'Com {nasc} anos: VOTO OPCIONAL'


# programa principal:
print('--'*20)
data = date.today().year - int(input('Em que ano você nasceu? '))
print(voto(data))