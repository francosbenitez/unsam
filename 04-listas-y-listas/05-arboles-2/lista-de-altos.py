"""
Ejercicio 4.19: Lista de altos de Jacarandá
Usando comprensión de listas y la variable arboleda podés por ejemplo armar la lista de la altura de los árboles.

H=[float(arbol['altura_tot']) for arbol in arboleda]
Usá los filtros (recordá la Sección 4.3) para armar la lista de alturas de los Jacarandás solamente.
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

H = [ float(arbol["altura_tot"]) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
