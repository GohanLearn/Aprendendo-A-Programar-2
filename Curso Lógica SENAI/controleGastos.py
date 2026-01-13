Gastos = []
print('Registre seus gastos diários da semana: ')
for i in range(0, 7):
    gDia = float(input(f'Gastos do dia {i+1}: R$ '))
    Gastos.append(f'Dia {i+1}: {gDia:.2f}')
for j in range(0, 7):
    print(Gastos[j])