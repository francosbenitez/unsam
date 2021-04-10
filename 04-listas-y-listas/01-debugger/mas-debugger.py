"""
Ejercicio 4.2: Más debugger
Siguiendo con los ejemplos del Ejercicio 3.1, usá el debugger para analizar el siguiente código:

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
Observá en particular lo que ocurre al leer la segunda fila de datos del archivo y guardarlos en la variable registro con los datos ya guardados en la lista camion.
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
#    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            # coloco el registro={} dentro del for para que
            # no me devuelva valores repetidos
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)