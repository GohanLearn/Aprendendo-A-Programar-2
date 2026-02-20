# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

# imports:
import requests

# programa principal:
try:
    requests.get('https://pudim.com')
except:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso.\033[m')