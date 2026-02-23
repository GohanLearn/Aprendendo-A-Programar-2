import os
from lib.interface import *

def arquivoExiste(nome):
    try:
        os.chdir(r"C:\Users\prisc\MeusProjetos\Aprendendo-A-Programar-2\Curso Python Gustavo Guanabara\Mundo 3\Aula #23 (Tratamento de Erros e Exceções)\desafio115")
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True


def criarArquivo(nome):
    os.chdir(r"C:\Users\prisc\MeusProjetos\Aprendendo-A-Programar-2\Curso Python Gustavo Guanabara\Mundo 3\Aula #23 (Tratamento de Erros e Exceções)\desafio115")
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome):
    os.chdir(r"C:\Users\prisc\MeusProjetos\Aprendendo-A-Programar-2\Curso Python Gustavo Guanabara\Mundo 3\Aula #23 (Tratamento de Erros e Exceções)\desafio115")
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade='0'):
    os.chdir(r"C:\Users\prisc\MeusProjetos\Aprendendo-A-Programar-2\Curso Python Gustavo Guanabara\Mundo 3\Aula #23 (Tratamento de Erros e Exceções)\desafio115")
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()