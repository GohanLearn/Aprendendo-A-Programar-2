from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)