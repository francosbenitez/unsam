"""
Ejercicio 5.2: Generala no necesariamente servida
Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo generala.py.

Extra: Hay gente que, si en la primera tirada le salen todos dados diferentes, los mete al cubilete y tira los cinco nuevamente. Otras personas, eligen uno de esos dados diferentes, lo guardan, y tiran sólo los cuatro restantes. ¿Podés determinar, por medio de simulaciones, si hay una de estas estrategias que sea mejor que la otra?
"""

import random

def tirar():
    return [random.randint(1, 6) for _ in range(5)]

def es_generala(tirada):
    return tirada.count(tirada[0]) == 5

def generala_tres():
    return sum([es_generala(tirar()) for _ in range(3)])

n_tiradas = 1000000
ganadas = sum([generala_tres() for _ in range(n_tiradas)])
prob = ganadas / n_tiradas
print(f'Tiré {n_tiradas} veces, de las cuales {ganadas} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida en tres tiradas mediante {prob:.6f}.')
