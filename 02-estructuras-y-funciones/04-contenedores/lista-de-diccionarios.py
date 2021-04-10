"""
Ejercicio 2.16: Lista de diccionarios
Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un diccionario en vez de una tupla. En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del archivo de entrada.

Experimentá con esta función nueva igual que en el ejercicio anterior.

>>> camion = leer_camion('../Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Limon', 'cajones': 150, 'precio': 83.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
>>> camion[0]
{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}
>>> camion[1]
{'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}
>>> camion[1]['cajones']
50
>>> total = 0.0
>>> for s in camion:
       total += s['cajones']*s['precio']

>>> print(total)
47671.15
>>>
Fijate que acá los distintos campos para cada entrada se acceden a través de claves en vez de la posición en la lista. Muchas veces preferimos esto porque el código resulta más fácil de leer. Tanto para otres como para nosotres en el futuro.

Mirar diccionarios y listas muy grandes puede ser un lío. Para limpiar el output para debuguear, probá la función pprint (Pretty-print) que le da un formato más sencillo de interpretar.

>>> from pprint import pprint
>>> pprint(camion)
[{'nombre': 'Lima', 'precio': 32.2, 'cajones': 100},
   {'nombre': 'Naranja', 'precio': 91.1, 'cajones': 50},
   {'nombre': 'Limon', 'precio': 83.44, 'cajones': 150},
   {'nombre': 'Mandarina', 'precio': 51.23, 'cajones': 200},
   {'nombre': 'Durazno', 'precio': 40.37, 'cajones': 95},
   {'nombre': 'Mandarina', 'precio': 65.1, 'cajones': 50},
   {'nombre': 'Naranja', 'precio': 70.44, 'cajones': 100}]
>>>
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
    return camion
    
camion = leer_camion("Data/camion.csv")
pprint(camion)
