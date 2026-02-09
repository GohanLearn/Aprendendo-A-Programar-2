# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

# bibliotecas:
from datetime import date


# funções:
def voto(nasc):
    if nasc >= 18:
        if nasc > 65:
            return 'OPCIONAL'
        else:
            return 'OBRIGATÓRIO'
    elif nasc < 16:
        return 'NEGADO'
    else:
        return 'OPCIONAL'


# programa principal:
print('--'*20)
data = date.today().year - int(input('Em que ano você nasceu? '))
print(f'Com {data} anos: VOTO {voto(data)}.')