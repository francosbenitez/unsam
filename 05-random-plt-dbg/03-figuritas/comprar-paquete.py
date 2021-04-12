"""
Ejercicio 5.15:
Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.

Ejercicio 5.16:
Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total) y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
"""

import random

def comprar_figu(figus_total):
    return random.randint(1, figus_total)-1

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for _ in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete

# figus_total = 670
# paquete = []
# for _ in range(5):
#     paquete.append(comprar_figu(figus_total))
    
figus_total = 670
figus_paquete = 5
comprar = comprar_paquete(figus_total, figus_paquete)
