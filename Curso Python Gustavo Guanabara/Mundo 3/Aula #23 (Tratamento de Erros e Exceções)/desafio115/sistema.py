from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print()
    elif resposta == 2:
        print()
    elif resposta == 3:
        print('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)