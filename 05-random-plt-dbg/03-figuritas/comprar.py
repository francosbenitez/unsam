"""
Ejercicio 5.11: Comprar
Alguna de las funciones que introdujimos en la Sección 5.1 sirve para devolver un número entero aleatorio dentro de un rango (¿cuál era?). Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
"""

import random
import numpy as np

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

crear = crear_album(670)

def comprar_figu(figus_total):
#    return random.randint(1, len(crear))
#    return random.randint(1, figus_total)
#    return random.randint(0, figus_total)
    return random.randint(1, figus_total)-1

comprar = comprar_figu(len(crear))

