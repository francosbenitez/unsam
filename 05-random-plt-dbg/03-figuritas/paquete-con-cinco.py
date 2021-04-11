"""
Ejercicio 5.15:
Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 670. Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.
"""

import random

def comprar_figu(figus_total):
    return random.randint(0, figus_total)

figus_total = 670
paquete = list()
for i in range(5):
    lote = comprar_figu(figus_total)
    paquete.append(lote)






