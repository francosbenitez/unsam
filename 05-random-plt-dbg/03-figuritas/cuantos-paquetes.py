"""
Ejercicio 5.17:
Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo.

Ejercicio 5.18:
Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 670, figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. Si te da la compu, hacelo con 1000 repeticiones.

Graficar el llenado del álbum
El siguiente código usa las funciones que hiciste antes para graficar la curva de llenado de un álbum a medida que comprás paquetes de figuritas. Es un primer ejemplo de gráfico de líneas. En las próximas clases estudiaremos los detalles sobre gráficos de una manera sistemática. Por ahora solo un botón de muestra.

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
"""

import random
import numpy as np
import matplotlib.pyplot as plt

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

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()