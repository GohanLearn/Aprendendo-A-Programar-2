# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
v = 'AEIOUaeiou'
for i in palavras:
    print(f'Na palavra {i.upper()} temos ', end = '')
    for n in i:
        if n in v:
         print(n, end = ' ')
    print('\n')