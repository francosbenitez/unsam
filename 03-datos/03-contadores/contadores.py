"""
Ejercicio 3.11: Contadores
Vamos a usar un contador (objeto Counter) para contar cajones de frutas. Probalo:

>>> camion = leer_camion('../Data/camion.csv')
>>> from collections import Counter
>>> tenencias = Counter()
>>> for s in camion:
        tenencias[s['nombre']] += s['cajones']

>>> tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
>>>
Observá que la entradas múltiples como Mandarina y Naranja en camion se combinan en una sola entrada.

Podés usar el contador como un diccionario para recuperar valores individuales:

>>> tenencias['Naranja']
150
>>> tenencias['Mandarina']
250
>>>
Podés listar las tres frutas con mayores tenencias:

>>> # Las 3 frutas con más cajones
>>> tenencias.most_common(3)
[('Mandarina', 250), ('Naranja', 150), ('Caqui', 150)]
>>>
Carguemos los datos de otro camión con cajones de fruta en un nuevo contador:

>>> camion2 = leer_camion('../Data/camion2.csv')
>>> tenencias2 = Counter()
>>> for s in camion2:
          tenencias2[s['nombre']] += s['cajones']

>>> tenencias2
Counter({'Durazno': 125, 'Frambuesa': 250, 'Lima': 50, 'Mandarina': 25})
>>>
Y finalmente combinemos las tenencias de ambos camiones con una operación simple:

>>> tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
>>> tenencias2
Counter({'Frambuesa': 250, 'Durazno': 125, 'Lima': 50, 'Mandarina': 25})
>>> combinada = tenencias + tenencias2
>>> combinada
Counter({'Caqui': 150, 'Durazno': 220, 'Frambuesa': 250, 'Lima': 150, 'Mandarina': 275, 'Naranja': 150})
>>>
"""

import csv
from collections import Counter

def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    camion = []
    for row in rows:
        lote = (row[0], int(row[1]), float(row[2]))
        camion.append(lote)
    return camion

camion = leer_camion("Data/camion.csv")
tenencias = Counter()
for nombre, n_cajones, precio in camion:
    tenencias[nombre] += n_cajones

camion2 = leer_camion("Data/camion2.csv")
tenencias2 = Counter()
for nombre, n_cajones, precio in camion2:
    tenencias2[nombre] += n_cajones
    
combinada = tenencias + tenencias2

print(tenencias)
print(tenencias2)
print(combinada)