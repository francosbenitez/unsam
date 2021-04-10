"""
Ejercicio 3.19: Determinar las especies en un parque
Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior y devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.

Sugerencia: Usá el comando set como en la Sección 2.4.
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

def especies(lista_arboles):
    informacionDeEspecies = set([])
    for row in lista_arboles:
        # solamente nombre_com
        lote = row["nombre_com"]
        # sumo todas las especies usando add
        informacionDeEspecies.add(lote)
    return informacionDeEspecies
    
especies = especies(leer_parque("Data/arbolado.csv", "GENERAL PAZ"))
print(especies)



