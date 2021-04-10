"""
Ejercicio 5.10: Incompleto
¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector que representa el álbum? ¿Qué significa que haya al menos un cero en nuestro vector?

Implemente la función album_incompleto(A) que recibe un vector y devuelve True si el vector contiene el elemento 0. En el caso en que no haya ceros debe devolver False.

Estas funciones son tan sencillas --cada una puede escribirse en una sola línea-- que podría ponerse directamente esa línea cada vez que queremos llamar a la función. Sin embargo, en esta etapa nos parece conveniente que organices el código en funciones, por más que sean sencillas.
"""

import numpy as np

def crear_album(figus_total):
    figus_total = np.zeros(figus_total, dtype=np.int64)
    return figus_total

crear = crear_album(670)

def album_incompleto(A):
    for elemento in A: 
        if elemento == 0:
            print(True)
            break
        else: 
            print(False)
            
incompleto = album_incompleto(crear)