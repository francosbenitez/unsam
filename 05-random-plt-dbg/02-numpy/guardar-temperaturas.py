"""
Ejercicio 5.7: Guardar temperaturas
Ampliá el código de termometro.py que escribiste en el Ejercicio 5.5 para que guarde el vector con las temperaturas simuladas en el directorio Data de tu carpeta de ejercicios, en un archivo llamado Temperaturas.npy. Hacé que corra 999 veces en lugar de solo 99.
"""

import random
import numpy as np

n = 999

termometro = []
for i in range(n):
    lote = random.normalvariate(37.5, 0.2)
    termometro.append(lote)

minimo = min(termometro)
maximo = max(termometro)
promedio = sum(termometro) / n
media = sorted(termometro)[int(len(termometro)/2)]

np.save("Data/temperaturas.npy", termometro)