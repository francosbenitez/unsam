"""
Ejercicio 4.18: Lectura de todos los árboles
Basándote en la función leer_parque(nombre_archivo, parque) del Ejercicio 3.18, escribí otra leer_arboles(nombre_archivo) que lea el archivo indicado y devuelva una lista de diccionarios con la información de todos los árboles en el archivo. La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos.

Vamos a llamar arboleda a esta lista.
"""

import csv

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
print(arboleda[1])

