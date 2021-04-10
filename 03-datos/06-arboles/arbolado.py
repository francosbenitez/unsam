"""
Ejercicio 3.18: Lectura de los árboles de un parque
Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del csv es un árbol).

Sugerencia: basate en la función leer_camion() y usá también el comando zip como hiciste en el Ejercicio 3.9 para combinar el encabezado del archivo con los datos de cada fila. Inicialmente no te preocupes por los tipos de datos de cada columna, pero cuando empieces a operar con una columna modificá esta función para que ese dato sea del tipo adecuado para operar.

Observación: La columna que indica el nombre del parque en el que se encuentra el árbol se llama 'espacio_ve' en el archivo CSV.

Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo, debería darte una lista con 690 árboles.
"""

import csv

def leer_parque(nombre_archivo, parque):
    informacionDeParques = list()
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        # agrego condicion
        if parque in row:
            lote = dict(zip(headers, row))
            informacionDeParques.append(lote)
    return informacionDeParques
    
parque = leer_parque("Data/arbolado.csv", "GENERAL PAZ")
print(parque)
