# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa.

# programa:
expressao = []
aberto = 0
expressao.append(str(input('Digite a expressão: ')))
for l in expressao[0]:
    if l == '(':
        aberto += 1
    elif l == ')':
        if aberto == 0:
            aberto -= 1
            break
        else:
            aberto -= 1
if aberto == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')