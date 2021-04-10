"""
Ejercicio 4.21: Diccionario con medidas
En este ejercicio vamos a considerar algunas especies de árboles. Por ejemplo:

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
Te pedimos que armes un diccionario en el que estas especies sean las claves y los valores asociados sean los datos que generaste en el ejercicio anterior. Más aún, organizá tu código dentro de una función medidas_de_especies(especies,arboleda) que recibe una lista de nombres de especies y una lista como la del Ejercicio 4.18 y devuelve un diccionario cuyas claves son estas especies y sus valores asociados sean las medidas generadas en el ejercicio anterior.

Vamos a usar esta función la semana próxima. A modo de control, si llamás a la función con las tres especies del ejemplo como parámetro (['Eucalipto', 'Palo borracho rosado', 'Jacarandá']) y la arboleda entera, deberías recibir un diccionario con tres entradas (una por especie), cada una con una lista asociada conteniendo 4112, 3150 y 3255 pares de números (altos y diámetros), respectivamente.

Acordate de guardar los ejercicios de esta sección en el archivo arboles.py.

Extra: casi todes usan un for para crear este diccionario. ¿Lo podés hacer usando una comprensión de diccionarios? Te recordamos la sintaxis: diccionario = { clave: valor for clave in claves }
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

def medidas_de_especies(especies, arboleda):
    diccionario = {}
    for especie in especies:
        medidas = []
        for arbol in arboleda: 
            if especie in arbol["nombre_com"]:
                lote = (float(arbol["altura_tot"]), 
                        float(arbol["diametro"]))
                medidas.append(lote)
                diccionario[especie] = medidas 
    return diccionario

diccionario = medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)
