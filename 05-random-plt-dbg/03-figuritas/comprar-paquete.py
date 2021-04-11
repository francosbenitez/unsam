"""
Ejercicio 5.16:
Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
"""

import random

def comprar_figu(figus_total):
    return random.randint(0, figus_total)

def comprar_paquete(figus_total, figus_paquete):
    paquete = list()
    for i in range(figus_paquete):
        lote = comprar_figu(figus_total)
        paquete.append(lote)
    return paquete
    
comprar = comprar_paquete(10, 600)
