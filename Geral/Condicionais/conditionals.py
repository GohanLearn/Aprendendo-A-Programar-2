#Obtendo informações sobre o sálario
salario = float(input ("Digite seu salário: ") )

#Condicionais
if salario <= 3000:
    print("Desenvolvedor Iniciante")
elif salario > 3000 and salario < 6000:
    print("Desenvolvedor Intermedário")
else:
    print("Desenvolvedor Avançado")