"""
Ejercicio 5.4: Calcular pi
Es interesante ver cómo los algoritmos estocásticos (basados en elecciones aleatorias) también sirven para resolver problemas que no tienen nada de estocásticos. En este ejercicio vas a usar el generador random() para aproximar pi.

Por definición pi es el área del círculo de radio uno. Si generamos puntos (x,y) con:

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y
tendremos puntos dentro del cuadrado [0, 1]x[0, 1]. Algunos de estos puntos del cuadrado caerán dentro del círculo unitario (los que cumplan que x^2 + y^2 < 1) y otros puntos caerán afuera. La proporción de puntos que caigan dentro del cuarto de círculo guardará relación con la proporción entre el área del cuarto de círculo y el área del cuadrado. Obviamente hay una componente aleatoria, pero a medida que la cantidad de puntos crece, la proporción de puntos se acercará a la proporción entre las dos áreas.

Puntos al azar dentro y fuera del circulo

Si el área del círculo completo es pi, el área de nuestro cuarto de círculo es pi/4. Por otro lado el área del cuadrado unitario es 1. Por lo tanto, si generamos N puntos con una distribución uniforme en el cuadrado unitario, esperamos que pi/4 de estos N puntos caigan dentro del cuarto del círculo y el resto afuera. Es decir que, si llamamos M al número de puntos que caen dentro del círculo, esperamos que M ~(pi/4 * N).

Despejando pi de esta estimación, obtenemos que pi ~ 4*M/N. Esto nos permite estimar pi mirando cuántos puntos caen realmente dentro del círculo del total de puntos.

Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la función generar_punto(), calcule la proporción de estos puntos que caen en el círculo unitario (usando ¿x^2 + y^2 < 1?) y use este resultado para dar una aproximación de pi.
"""

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y 

n = 100000
m = 0
for _ in range(n):
    x, y = generar_punto()
    if x ** 2 + y ** 2 < 1:
        m += 1
        
print(f"pi {4*m/n:.5f}")

