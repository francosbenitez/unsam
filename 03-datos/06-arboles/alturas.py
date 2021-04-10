"""
Ejercicio 3.21: Alturas de una especie en una lista
Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior y una especie de árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas (columna 'altura_tot') de los ejemplares de esa especie en la lista.

Observación: Acá sí, fijate de devolver las alturas como números (de punto flotante) y no como cadenas de caracteres. Podés hacer esto modificando leer_parque.

Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en los tres parques mencionados.

Resultados de alturas de Jacarandás en tres parques:

Medida	General Paz	Los Andes	Centenario
max	16.0	25.0	18.0
prom	10.2
"""

import csv
from statistics import mean

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

def obtener_alturas(lista_arboles, especie):
    informacionDeAlturas = []
    # devuelve diccionarios
    for row in lista_arboles:
        # si la especie esta en la fila de especies
        if especie in row["nombre_com"]:
            # igualar el conjunto a la altura_total
            lote = int(row["altura_tot"])
            # agrego el lote a la lista
            informacionDeAlturas.append(lote)
    return informacionDeAlturas
    
alturasGeneralPaz = obtener_alturas(leer_parque("Data/arbolado.csv", "GENERAL PAZ"), "Jacarandá")
alturasLosAndes = obtener_alturas(leer_parque("Data/arbolado.csv", "ANDES, LOS"), "Jacarandá")
alturasCentenario = obtener_alturas(leer_parque("Data/arbolado.csv", "CENTENARIO"), "Jacarandá")

print(max(alturasGeneralPaz), max(alturasLosAndes), max(alturasCentenario))
print(mean(alturasGeneralPaz), round(mean(alturasLosAndes), 2), round(mean(alturasCentenario), 2))