# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC  e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

# programa:

# obtendo dados:
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura(m) : '))

# calculando imc:
imc = peso / altura ** 2
print(f'O seu IMC é de {imc}')
# respondendo:
if imc < 18.5:
    print('\033[1;31mAbaixo do peso.\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[1;32mPeso ideal.\033[m')
elif imc >= 25 and imc < 30:
    print('\033[1;33mSobrepeso.\033[m')
elif imc >= 30 and imc <= 40:
    print('\033[1;34mObesidade.\033[m')
else:
    print('\033[1;31mObesidade mórbida.\033[m')