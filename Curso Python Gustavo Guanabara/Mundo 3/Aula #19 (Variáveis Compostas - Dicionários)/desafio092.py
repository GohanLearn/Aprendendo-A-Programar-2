# Crie umm programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos de colaboração)

# bibliotecas:
import datetime

# programa:
contribuidor = dict()
contribuidor['nome'] = str(input('Nome: '))
contribuidor['idade'] = datetime.date.today().year - int(input('Ano de Nascimento: '))
contribuidor['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if contribuidor['ctps'] != 0:
    contribuidor['contratação'] = int(input('Ano de contratação: '))
    contribuidor['salário'] = float(input('Salário: R$ '))
    contribuidor['aposentadoria'] = contribuidor['idade'] - (datetime.date.today().year - contribuidor['contratação']) + 35
print('-=-'*20)
for k, v in contribuidor.items():
    print(f'{k} tem valor {v}')