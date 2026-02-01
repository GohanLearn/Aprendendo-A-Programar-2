# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# -------------
#  Olá, Mundo!
# -------------

# funções:
def escreva(txt):
    for l in txt:
        print('-', end='')
    print()
    print(txt)
    for l in txt:
        print('-', end='')
    print()

# programa principal:
escreva(' Curso em Video ')
escreva('Gustavo')