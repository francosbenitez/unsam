"""
Ejercicio 3.22: Inclinaciones por especie de una lista
Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de árbol y una lista de árboles como la anterior, devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie.
"""

import csv

def leer_parque(nombre_archivo, parque):
    informacionDeParques = list()
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        if parque in row:
            lote = dict(zip(headers, row))
            informacionDeParques.append(lote)
    return informacionDeParques
    
parque = leer_parque("Data/arbolado.csv", "GENERAL PAZ")

def obtener_inclinaciones(lista_arboles, especie):
    informacionDeInclinaciones = []
    for row in lista_arboles:
        if especie in row["nombre_com"]:
            lote = int(row["inclinacio"])
            informacionDeInclinaciones.append(lote)
    return informacionDeInclinaciones
    
inclinaciones = obtener_inclinaciones(parque, "Jacarandá")
print(inclinaciones)
