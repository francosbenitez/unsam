"""
Ejercicio 5.9: Crear
Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas.
"""

import numpy as np

def crear_album(figus_total):
    figus_total = np.zeros(figus_total, dtype=np.int64)
    return figus_total

crear = crear_album(670)


            

