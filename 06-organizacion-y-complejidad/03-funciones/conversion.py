"""
Ejercicio 6.8: Conversión de tipo
Modificá la función parse_csv() de modo que permita, opcionalmente, convertir el tipo de los datos recuperados antes de devolverlos.

>>> camion = parse_csv('../Data/camion.csv', types=[str, int, float])
>>> camion
[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]

>>> cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
>>> cajones_lote
[{'nombre': 'Lima', 'cajones': 100}, {'nombre': 'Naranja', 'cajones': 50}, {'nombre': 'Caqui', 'cajones': 150}, {'nombre': 'Mandarina', 'cajones': 200}, {'nombre': 'Durazno', 'cajones': 95}, {'nombre': 'Mandarina', 'cajones': 50}, {'nombre': 'Naranja', 'cajones': 100}]
>>>
Ya vimos esto en el Ejercicio 4.12. Vas a necesitar insertar la siguiente porción de código en tu implementación:

...
if types:
    fila = [func(val) for func, val in zip(types, fila) ]
...
"""

import csv

def parse_csv(nombre_archivo, select = None, types=[str, int, float]):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        if types:
            filas = [func(val) for func, val in zip(types, filas)]
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila: 
                continue
            if indices:
                fila = [fila[index] for index in indices]
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    return registros

camion = parse_csv('Data/camion.csv', types=[str, int, float])
cajones_lote = parse_csv('Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])

