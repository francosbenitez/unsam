"""
Ejercicio 2.6: Transformar un script en una función
Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) en una función costo_camion(nombre_archivo). Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión y devuelve el costo de la carga de frutas como una variable de punto flotante.

Para usar tu función, cambiá el programa de forma que se parezca a esto:

def costo_camion(nombre_archivo):
   ...
    # Tu código
   ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
Cuando ejecutás tu programa, deberías ver la misma salida impresa que antes. Una vez que lo hayas corrido, podés llamar interactivamente a la función escribiendo esto:

bash $ python3 -i costo_camion.py
Esto va a ejecutar el código en el programa y dejar abierto el intérprete interactivo.

>>> costo_camion('Data/camion.csv')
47671.15
>>>
Es útil para testear y debuguear poder interactuar interactivamente con tu código.
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    i = 0
    costo = 0
    for row in rows:
        cajones = int(row[1])
        precio = float(row[2])
        costo += cajones * precio
        i = i + 1 
    return costo
    
costo = costo_camion("Data/camion.csv")
print("Costo total:", costo)