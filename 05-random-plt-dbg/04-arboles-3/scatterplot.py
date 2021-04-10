"""
Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás
En este ejercicio introducimos un nuevo tipo de gráfico: el gráfico de dispersión o scatterplot. El mismo usa coordenadas cartesianas para mostrar los valores de dos variables para un conjunto de datos.

En este caso vamos a graficar un punto en el plano (x,y) por cada árbol en el dataset (o para cada arbol de cierta especie). El punto correspondiente a un árbol con diámetro d y altura h será ubicado en la posición x=d y y=h. Este tipo de gráfico permite visualizar relaciones o tendencias entre las variables y es muy útil en el análisis exploratorio de datos.

Usando como base tu trabajo del Ejercicio 4.20, vas a generar un scatterplot para visualizar la relación entre diámetro y alto de los Jacarandás del dataset.

Si ya tenés una lista o un vector d con diámetros y otra h con altos, es sencillo hacer un primer scatterplot:

import matplotlib.pyplot as plt
plt.scatter(d,h)
Algunas recomendaciones:

Convertí la lista generada en un ndarray de numpy, de esa forma podés usar rebanadas para obtener un vector d con diámteros y otro h con alturas inmediatamente.
Mirá algún ejemplo como este y tratá de entender cómo se usan los parámetros opcionales s (de size, tamaño) y c (de color) y alpha (de transparencia) de la función matplotlib.pyplot.scatter.
Usando el parámetro alpha hacé que el gráfico permita visualizar dónde hay mayor densidad de datos.
¿Ves alguna relación entre el diámetro y el alto de los Jacarndás? ¿Te parece que es una relación lineal o de otro tipo?

Agregale nombres a los ejes y a la figura usando los siguientes comandos:

plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    arboles = list()
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        arboles.append(lote)
    return arboles

arboleda = leer_arboles("Data/arbolado.csv")

alt_diam_jac = [ (float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
h = np.array(alt_diam_jac)[:,0] # convertir los diccionarios a array
d = np.array(alt_diam_jac)[:,1]
plt.scatter(d, h, alpha = 0.3)
plt.title("gg")