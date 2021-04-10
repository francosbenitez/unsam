"""
Ejercicio 2.18: Balances
Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios()) y completá el programa para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17) calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.
"""

import csv

def leer_camion(nombre_archivo):
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
    return camion

def leer_precios(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    diccionario = {}
    for row in rows:
        try:  
            fruta = row[0]
            precio = float(row[1])
            diccionario[fruta] = precio
        except:
            continue
    return diccionario

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo = 0
    for row in rows:
        cajones = int(row[1])
        precio = float(row[2])
        costo += cajones * precio
    return costo

def buscar_precio(fruta_buscada):
    f = open("Data/precios.csv", "rt")
    precio = 0
    for line in f:
        row = line.strip('\n').split(',')
        fruta = row[0]
        precio_fruta = row[-1]
        if fruta == fruta_buscada:
                precio = precio_fruta
    return float(precio)

camion = leer_camion("Data/camion.csv")
costo_camion = costo_camion("Data/camion.csv")
recaudacion = 0
for producto in camion:
    nombre = float(buscar_precio(producto["nombre"]))
    cajones = int(producto["cajones"])
    recaudacion += nombre * cajones

diferencia = recaudacion - costo_camion
mensaje = f"Costo del camion: {costo_camion} | Recaudacion: {recaudacion} | Ganancia: {diferencia:.2f}"
print(mensaje)










