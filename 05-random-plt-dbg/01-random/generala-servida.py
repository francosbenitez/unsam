"""
Ejercicio 5.1: Generala servida
Queremos estimar la probabilidad de obtener una generala servida (cinco dados iguales) en una tirada de dados. Podemos hacer la cuenta usando un poco de teoría de probabilidades, o podemos simular que tiramos los dados muchas veces y ver cuántas de esas veces obtuvimos cinco dados iguales. En este ejercicio vamos a usar el segundo camino.

Escribí una función tirar() que devuelva una lista con cinco dados generados aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve True si y sólo si los cinco dados de la lista tirada son iguales.

Luego analizá el siguiente código. Correlo con N = 100000 varias veces y observá los valores que obtenés. Luego correlo algunas veces con N = 1000000 (ojo, hace un millón de experimentos, podría tardar un poco):

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000? ¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? ¿Cómo se puede calcular la probabilidad de forma exacta?
"""

import random

def tirar():
    tirada=[]
    for _ in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

# usando comprension de listas
def tirar_2():
    return [random.randint(1, 6) for _ in range(5)]

def es_generala(tirada):
    return tirada.count(tirada[0]) == 5
#    return max(tirada) == min(tirada)

n_tiradas = 1000000
ganadas = sum([es_generala(tirar_2()) for _ in range(n_tiradas)])
prob = ganadas / n_tiradas
print(f'Tiré {n_tiradas} veces, de las cuales {ganadas} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    
