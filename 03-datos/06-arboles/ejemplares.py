"""
Ejercicio 3.20: Contar ejemplares por especie
Usando contadores como en el Ejercicio 3.11, escribí una función contar_ejemplares(lista_arboles) que, dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies (recordá, es la columna 'nombre_com' del archivo) sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.

Luego, combiná esta función con leer_parque() y con el método most_common() para informar las cinco especies más frecuentes en cada uno de los siguientes parques:

'GENERAL PAZ'
'ANDES, LOS'
'CENTENARIO'
Resultados de cantidad por especie en tres parques:

General Paz	Los Andes	Centenario
Casuarina: 97	Jacarandá: 117	Plátano: 137
Tipa blanca: 54	Tipa blanca: 28	Jacarandá: 45
Eucalipto: 49	Ciprés: 21	Tipa blanca: 42
Palo borracho rosado: 44	Palo borracho rosado: 18	Palo borracho rosado: 41
Fenix: 40	Lapacho: 12	Fresno americano: 38
"""

import csv
from collections import Counter

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

def contar_ejemplares(lista_arboles):
    informacionEjemplares = Counter()
    for row in lista_arboles:
        lote = row["nombre_com"]
        # sumo todos los ejemplares usando el 1
        informacionEjemplares[lote] += 1
    return informacionEjemplares
    
ejemplaresGeneralPaz = contar_ejemplares(leer_parque("Data/arbolado.csv", "GENERAL PAZ"))
ejemplaresLosAndes = contar_ejemplares(leer_parque("Data/arbolado.csv", "ANDES, LOS"))
ejemplaresCentario = contar_ejemplares(leer_parque("Data/arbolado.csv", "CENTENARIO"))

ejemplaresMasComunesGeneralPaz = ejemplaresGeneralPaz.most_common(5)
ejemplaresMasComunesLosAndes = ejemplaresLosAndes.most_common(5)
ejemplaresMasComunesCentenario = ejemplaresCentario.most_common(5)

print(ejemplaresMasComunesGeneralPaz)
print(ejemplaresMasComunesLosAndes)
print(ejemplaresMasComunesCentenario)