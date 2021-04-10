"""
Ejercicio 5.24: Histograma de altos de Jacarandás
Usando tu trabajo en el Ejercicio 4.19, generá un histograma con las alturas de los Jacarandás en el dataset.

Tu código debería verse similar a este:

import os
import matplotlib.pyplot as plt
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [comprensión de listas]
plt.hist(altos,bins=...)
Observación: Spyder tiene opciones para mostrar las figuras dentro de la misma ventana o en una ventana nueva (Tools -> Preferences -> IPython console -> Graphics -> Backend). Te recomendamos generarlas en una ventana nueva. Luego, con plt.clf() podés borrar la figura actual y con plt.figure() generás una nueva figura por si querés dejar varias abiertas a la vez.
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

alt_jac = [ float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
alt_diam_jac = [ (float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
plt.hist(alt_jac, bins = 20)
plt.xlabel("Alto/cm")
plt.ylabel("Num.Individuos")

