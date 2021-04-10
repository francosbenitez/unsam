"""
Ejercicio 2.15: Lista de tuplas
El archivo Data/camion.csv contiene la lista de cajones cargados en un camión. En el Ejercicio 2.6 de la sección anterior escribiste una función costo_camion(nombre_archivo) que leía el archivo y realizaba un cálculo.

La función debería verse parecida a ésta:

fragmento de costo_camion.py
import csv
...

def costo_camion(nombre_archivo):
   '''Computa el precio total del camion (cajones * precio) de un archivo'''
   total = 0.0

   with open(nombre_archivo, 'rt') as f:
       rows = csv.reader(f)
       headers = next(rows)
       for row in rows:
           ncajones = int(row[1])
           precio = float(row[2])
           total += ncajones * precio
   return total

...
Usando este código como guía, creá un nuevo archivo informe.py. En este archivo, definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas. Para hacerlo vas a tener que hacer algunas modificaciones menores al código de arriba.

Primero, en vez de definir total = 0, tenés que empezar con una variable que empieza siendo una lista vacía Por ejemplo:

camion = []
Después, en vez de sumar el costo, tenés que pasar cada fila a una tupla igual a como lo hiciste en el último ejercicio, y agregarla a la lista. Por ejemplo:

for row in rows:
   lote = (row[0], int(row[1]), float(row[2]))
   camion.append(lote)
Por último, la función debe devolver la lista camion.

Experimentá con tu función interactivamente (acordate de que primero tenés que correr el programa informe.py en el intérprete):

Ayuda: Usá -i para ejecutar un archivo en la terminal y quedar en el intérprete

>>> camion = leer_camion('../Data/camion.csv')
>>> camion
[('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Limon', 150, 83.44), ('Mandarina', 200, 51.23),('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]
>>>
>>> camion[0]
('Lima', 100, 32.2)
>>> camion[1]
('Naranja', 50, 91.1)
>>> camion[1][1]
50
>>> total = 0.0
>>> for s in camion:
       total += s[1] * s[2]

>>> print(total)
47671.15
>>>
Esta lista de tuplas que creaste es muy similar a un array o matriz bidimensional. Por ejemplo, podés acceder a una fila específica y columna específica usando una búsqueda como camion[fila][columna] donde fila y columna son números enteros.

También podés reescribir el último ciclo for usando un comando como éste:

>>> total = 0.0
>>> for nombre, cajones, precio in camion:
           total += cajones*precio

>>> print(total)
47671.15
>>>
Observación: la instrucción += es una abreviación. Poner a += b es equivalente a poner a = a + b
"""

import csv

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
print("Camion:", camion)