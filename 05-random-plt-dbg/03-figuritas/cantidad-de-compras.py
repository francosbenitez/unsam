"""
Ejercicio 5.12: Cantidad de compras
Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total), genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.

Ejercicio 5.13:
Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y guardá en una lista los resultados obtenidos en cada repetición. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.

Ayuda: El comando np.mean(l) devuelve el promedio de la lista l.

¿Podés crear esta lista usando una comprensión de listas?

Ejercicio 5.14:
Calculá n_repeticiones=100 veces la función cuantas_figus(figus_total=670) y guardá los resultados obtenidos en cada repetición en una lista. Con los resultados obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum (de 670 figuritas).

Guardá todo lo que hiciste hasta aquí sobre figuritas en un archivo figuritas.py. Lo que sigue profundiza un poco más en el asunto.
"""

import random
import numpy as np

def crear_album(figus_total):
    figus_total = np.zeros(figus_total, dtype=np.int64)
    return figus_total

def album_incompleto(A):
    return not A.all()

def comprar_figu(figus_total):
    return random.randint(0, figus_total)

def cuantas_figus(figus_total):
    album_nuevo = crear_album(figus_total)
    contador = 0
    while album_incompleto(album_nuevo) == True:
        figurita_comprada = comprar_figu(figus_total)
        album_nuevo[figurita_comprada-1] += 1
        contador += 1
    return contador

n_repeticiones = 1000 
figus_total = 6
resultados = []
for i in range(n_repeticiones):
    lote = cuantas_figus(figus_total)
    resultados.append(lote)

promedio_1 = np.mean(resultados)
print(promedio_1)

n_repeticiones = 100
figus_total = 670
resultados = []
for i in range(n_repeticiones):
    lote = cuantas_figus(figus_total)
    resultados.append(lote)

promedio_2 = np.mean(resultados)
print(promedio_2)
