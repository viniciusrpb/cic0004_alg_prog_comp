#O volume de uma esfera com raio r é 4/3 \pi r^3..
#Qual é o volume de uma esfera com raio 'r' (entrada do usuário [float])?
import math

#Entrada
raio = float(input("Informe o valor do raio: "))

#Computacao
volume = 4/3 * math.pi * raio**3

#Saida
print(f"O volume de uma esfera com raio {raio} é: {volume:.2f}")