# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.

# programa
frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split() # separa as palavras
junto = ''.join(palavras) # remove espaços
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
print(junto)
if inverso == junto:
    print('É um políndromo.')
else:
    print('Não é um polídromo.')