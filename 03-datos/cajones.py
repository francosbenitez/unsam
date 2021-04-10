"""
Script de prueba: Devolver todos las frutas que tengan 100 cajones.
"""

import csv

def leer_camion(nombre_archivo, cajones):
    informacionDeCajones = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        if cajones in row:
            lote = dict(zip(headers, row))
            informacionDeCajones.append(lote)
    return informacionDeCajones

cajones = leer_camion("Data/camion.csv", "100")
print(cajones)
    


