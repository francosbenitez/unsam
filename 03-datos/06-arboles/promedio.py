
"""
Ejercicio 3.24: Especie más inclinada en promedio
Volvé a combinar las funciones anteriores para escribir la función especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado..

Resultados. Deberías obtener, por ejemplo, que los Álamos Plateados del Parque Los Andes tiene un promedio de inclinación de 25 grados.
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
    
parque = leer_parque("Data/arbolado.csv", "ANDES, LOS")

def especies(lista_arboles):
    informacionDeEspecies = set([])
    for row in lista_arboles:
        lote = row["nombre_com"]
        informacionDeEspecies.add(lote)
    return informacionDeEspecies

def obtener_inclinaciones(lista_arboles, especie):
    informacionDeInclinaciones = []
    for row in lista_arboles:
        if especie in row["nombre_com"]:
            lote = int(row["inclinacio"])
            informacionDeInclinaciones.append(lote)
    return informacionDeInclinaciones

def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones = []
    nombres = []
    nombres = especies(lista_arboles)
    for especie in nombres:
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        promedio = round(sum(inclinacion)/int(len(inclinacion)))
        inclinaciones.append(promedio)
        promedios = dict(zip(nombres, inclinaciones))
        promedios = list(zip(promedios.values(), promedios.keys()))
        promedios = max(promedios)
    return promedios

promedios = especie_promedio_mas_inclinada(parque)
print(f"{promedios[1]} {promedios[0]}")