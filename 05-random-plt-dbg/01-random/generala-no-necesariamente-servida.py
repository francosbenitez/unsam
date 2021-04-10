"""
Ejercicio 5.2: Generala no necesariamente servida
Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los dados que más se repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida. Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un archivo generala.py.

Extra: Hay gente que, si en la primera tirada le salen todos dados diferentes, los mete al cubilete y tira los cinco nuevamente. Otras personas, eligen uno de esos dados diferentes, lo guardan, y tiran sólo los cuatro restantes. ¿Podés determinar, por medio de simulaciones, si hay una de estas estrategias que sea mejor que la otra?
"""

import random

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    return max(tirada) == min(tirada)

def generala_tres():
    G = sum([es_generala(tirar()) for i in range(3)])
    return True if G > 0 else False

N = 1000000
G = sum([generala_tres() for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida en tres tiradas mediante {prob:.6f}.')
