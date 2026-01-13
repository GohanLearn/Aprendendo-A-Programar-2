# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se ele já passou do tempo do alistamento
# Seu programa também deverá mostrar mostrar o tempo que falta ou que passou do prazo

# importando bibliotecas:
import datetime

# variáveis globais
anoAtual = datetime.date.today().year

# obtendo idade:
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - nascimento

# respondendo
if idade < 18:
    print(f'Você poderá se alistar em {nascimento+18}.')
elif idade == 18:
    print(f'Você já deve se alistar, pois tem {idade} anos.')
else:
    print(f'Você já passou do tempo do alistamento, que era em {nascimento+18}.')