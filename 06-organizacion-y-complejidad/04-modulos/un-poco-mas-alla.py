"""
Ejercicio 6.12: Un poco más allá
En Ejercicio 2.6 escribiste el programa costo_camion.py que lee, mediante una función llamada costo_camion() los datos de un camión y calcula su costo.

>>> import costo_camion
>>> costo_camion.costo_camion('../Data/camion.csv')
47671.15
>>>
Modificá el archivo costo_camion.py para que use la función informe.leer_camion() del programa informe_funciones.py.
"""

import informe_funciones as informe

def costo_camion(nombre_archivo):
    rows = informe.leer_camion(nombre_archivo)
    i = 0
    costo = 0
    for row in rows:
        cajones = int(row["cajones"])
        precio = float(row["precio"])
        costo += cajones * precio
        i = i + 1 
    return costo
    
costo = costo_camion("Data/camion.csv")
print("Costo total:", costo)
