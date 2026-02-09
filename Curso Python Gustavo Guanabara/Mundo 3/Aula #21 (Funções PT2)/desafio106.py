# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# OBS: use cores.


# variáveis globais
cores = {
    'red': '\033[1;30;41m',
    'white': '\033[7m',
    'green': '\033[1;30;42m',
    'blue': '\033[1;30;44m',
    'limpa': '\033[m'
}


# funções:
def enfeite(txt, cor):
    global cores
    tam = len(txt) + 4
    print(f'{cor}~'*tam)
    print(f' {txt} ')
    print('~'*tam, f'{cores['limpa']}')

# programa principal:
while True:
    enfeite('SISTEMA DE AJUDA PyHELP', cores['green'])
    ajuda = str(input('Função ou Biblioteca > ')).strip()
    if ajuda == 'FIM' or ajuda == 'fim':
        break
    enfeite(f"Acessando o manual do comando '{ajuda}'", cores['blue'])
    print(cores['white'])
    help(ajuda)
    print(cores['limpa'])
enfeite('ATÉ LOGO!', cores['red'])