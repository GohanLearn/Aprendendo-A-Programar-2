# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa.

# programa:
expressao = []
aberto = False
fechado = False
abertos = 0
fechados = 0
expressao.append(str(input('Digite a expressão: ')))
for l in expressao:
    if l == '(':
        abertos += 1
        aberto = True
        fechado = False
    elif l == ')':
        if aberto == True:
            fechados += 1
            fechado = True
            aberto = False
        else:
            fechado = False
if aberto == False and fechado == True and abertos == fechados:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')