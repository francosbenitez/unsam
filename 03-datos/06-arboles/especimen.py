"""
Ejercicio 3.23: Especie con el ejemplar más inclinado
Combinando la función especies() con obtener_inclinaciones() escribí una función especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación.

Correlo para los tres parques mencionados anteriormente.

Resultados. Deberías obtener, por ejemplo, que en el Parque Centenario hay un Falso Guayabo inclinado 80 grados.
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
    
parque = leer_parque("Data/arbolado.csv", "CENTENARIO")

def especimen_mas_inclinado(lista_arboles):
    especimenMasInclinado = []
    inclinacion = 0
    for row in lista_arboles:
        if inclinacion <= int(row["inclinacio"]):
            inclinacion = int(row["inclinacio"])
            nombre = row["nombre_com"]
            especimenMasInclinado = nombre, inclinacion
    return especimenMasInclinado

especimen = especimen_mas_inclinado(parque)
print(especimen)

