"""
Ejercicio 5.17:
Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

Ejercicio 5.18:
Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670, figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. Si te da la compu, hacelo con 1000 repeticiones.
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

def comprar_paquete(figus_total, figus_paquete):
    paquete = list()
    for i in range(figus_paquete):
        lote = comprar_figu(figus_total)
        paquete.append(lote)
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    cant_compras = 0
    album = crear_album(figus_total) 
    while album_incompleto(album) == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        cant_compras += 1
        for i in range(figus_paquete-1):
            album[paquete[i]-1] += 1
    return cant_compras

n_repeticiones = 100
figus_total = 670
figus_paquete = 5
resultados = []
for i in range(n_repeticiones):
    lote = cuantos_paquetes(figus_total, figus_paquete)
    resultados.append(lote)

promedio = np.mean(resultados)
print(promedio)