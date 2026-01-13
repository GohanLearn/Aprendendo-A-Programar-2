# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre a hipotenusa.
import math
catetoO = float(input('Comprimento do cateto oposto: '))
catetoA = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetoO, catetoA)
print(hipotenusa)