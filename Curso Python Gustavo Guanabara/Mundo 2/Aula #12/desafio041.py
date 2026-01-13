# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

# importando bibliotecas:
import datetime

# lendo ano de nascimento:
anoNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.date.today().year
ano = anoAtual - anoNascimento

# analisando e respondendo:
if ano <= 9:
    print('Você é um atleta da categoria \033[1;31mMirim\033[m!')
elif ano > 9 and ano <= 14:
    print('Você é um atleta da categoria \033[1;33mInfantil\033[m!')
elif ano > 14 and ano <= 19:
    print('Você é um atleta da categoria \033[1;35mJunior\033[m!')
else:
    print('Você é um atleta da categoria \033[1;31mMaster\033[m!')