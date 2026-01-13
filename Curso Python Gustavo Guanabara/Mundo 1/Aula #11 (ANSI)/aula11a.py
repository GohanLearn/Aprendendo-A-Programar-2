# apresentação
'\033[0;30;41' # texto basico branco fundo vermelho
'\033[4;33;44m' # texto sublinhado amarelo fundo azul
'\033[1;35;43m' # texto negrito roxo fundo amarelo
'\033[30;42m' # texto basico branco fundo verde
'\033[m' # basico do terminal, texto cinza e fundo preto
'\033[7;30m' # inverte as cores, texto preto fundo branco

# testando
#print('\033[7mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
print('\n')
nome = 'Guanabara'
print(f'Olá! Muito prazer em te conhecer, {'\033[31m'}{nome}{'\033[m'}!!!')
print('\n')
# testando mais
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print(f'Olá! Muito prazer em te conhecer, {cores['amarelo']}{nome}{cores['limpa']}!!!')