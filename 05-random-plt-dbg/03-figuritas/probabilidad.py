"""
Ejercicio 5.19:
Utilizando lo implementado en el ítem anterior, estimá la probabilidad de completar el álbum con 850 paquetes o menos.

Sugerencia: No leas esto antes de hacer el ejercicio. Hacelo primero y luego miralo. En este ejercicio resulta más compacto usar n_paquetes_hasta_llenar=np.array(lista) para convertir a vector la lista conteniendo cuántos paquetes compraste en cada experimento hasta llenar el álbum. Trabajar con vectores tiene ventajas. Por ejemplo probá la siguiente instrucción:

(n_paquetes_hasta_llenar <= 850).sum()

Ejercicio 5.20: Plotear el histograma
Usá un código similar al del Ejercicio 5.8 para hacer un histograma de la cantidad de paquetes que se compraron en cada experimeto, ajustando la cantidad de bins para que el gráfico se vea lo mejor posible.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

def album_incompleto(album):
    return 0 in album

def comprar_figu(figus_total):
    return random.randint(1, figus_total)-1

def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for _ in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
    return album.sum()/figus_paquete

figus_total = 670
n_repeticiones = 100
figus_paquete = 5

resultados = []
for _ in range(n_repeticiones):
    resultados.append(cuantos_paquetes(figus_total, figus_paquete))
    
promedio = np.mean(resultados)
print(f"Para llenar un album de {figus_total} figus compré en promedio {promedio} figus ({n_repeticiones} repeticiones)")

n_paquetes_hasta_llenar = np.array(np.array(resultados))
(n_paquetes_hasta_llenar <= 850).sum()/n_repeticiones
print(n_paquetes_hasta_llenar)

# histograma
plt.hist(n_paquetes_hasta_llenar, bins = 50)

# histograma de densidad
plt.hist(n_paquetes_hasta_llenar, bins = 50, density = True)

np.percentile(n_paquetes_hasta_llenar, 90)

# otra forma
n_paquetes_hasta_llenar.sort()
n_paquetes_hasta_llenar[int(0.9 * len(n_paquetes_hasta_llenar))]
