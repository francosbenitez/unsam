"""
Ejercicio 5.8: Empezando a plotear
En un rato vamos a empezar a hacer gráficos con Python. Aquí solo un botón de muestra.

Escribí un archivo plotear_temperaturas.py que lea el archivo de datos Temperaturas.npy con 999 mediciones simuladas que creaste recién y, usando el siguiente ejemplo, hacé un histograma de las temperaturas simuladas:

import matplotlib.pyplot as plt
plt.hist(temperaturas,bins=25)
Ajustá la cantidad de bins para que el gráfico se vea lo mejor posible.
"""

import numpy as np
import matplotlib.pyplot as plt

mediciones = np.load('Data/Temperaturas.npy')
plt.hist(mediciones, bins=25)
plt.show()