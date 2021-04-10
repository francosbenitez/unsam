"""
Ejercicio 4.20: Lista de altos y diámetros de Jacarandá
En el ejercicio anterior usaste una sola linea para seleccionar las alturas de los Jacarandás en parques porteños. Ahora te proponemos que armes una nueva lista que tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino también el diámetro de cada Jacarandá en la lista.

Esperamos que obtengas una lista similar a esta:

[(5.0, 10.0),
 (5.0, 10.0),
 ...
 (12.0, 25.0),
 ...
 (7.0, 97.0), 
 (8.0, 28.0), 
 (2.0, 30.0), 
 (3.0, 10.0), 
 (17.0, 40.0)]
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

H = [ (float(arbol["altura_tot"]), float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

