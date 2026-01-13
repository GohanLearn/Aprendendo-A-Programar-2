# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite um ângulo: '))
# Python usa radianos, não angulos, por isso devemos converter
rad = math.radians(angulo)

seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print(f'O seno é {seno:.2f} , o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f} .')