# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa.

# programa:
expressao = []
valida = True
aberto = 0
expressao.append(str(input('Digite a expressão: ')))
for l in expressao:
    if aberto < 0:
        valida = False
        break
    elif l == '(':
        aberto += 1
    elif l == ')':
        aberto -= 1
if aberto == 0:
    valida = True
else:
    valida = False
if valida:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')