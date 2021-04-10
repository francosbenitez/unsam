"""
Ejercicio 3.3: Un ejemplo práctico de enumerate()
Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan. Usando enumerate(), modificá tu programa costo_camion.py de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta.

>>> cost = costo_camion('../Data/missing.csv')
Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
Fila 7: No pude interpretar: ['Naranja', '', '70.44']
>>>
Para hacer esto, vas a tener que cambiar algunas partes de tu código.

...
for n_fila, fila in enumerate(filas, start=1):
    try:
        ...
    except ValueError:
        print(f'Fila {n_fila}: No pude interpretar: {fila}')
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo = 0
    for n_row, row in enumerate(rows, start=1):
        try:
            cajones = int(row[1])
            precio = float(row[2])
            costo += cajones * precio
            print(n_row, row)
        except ValueError:
            print(f"Fila {n_row}: No pude interpretar. {row}")
    return costo
    
costo = costo_camion("Data/missing.csv")
print("Costo total:", costo)
