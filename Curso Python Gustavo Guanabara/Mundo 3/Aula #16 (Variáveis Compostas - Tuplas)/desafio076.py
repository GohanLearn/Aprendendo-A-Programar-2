# Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# programa:
listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.75, 'Compasso', 9.99, 'Estojo', 25)
print('-'*40)
print('LISTAGEM DE PREÇOS'.center(40))
print('-'*40)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i].ljust(40, '.')}R$ {listagem[i-1]:>7.2f}')
print('-'*40)