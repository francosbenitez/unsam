"""
Ejercicio 7.4: De archivos a "objetos cual archivos"
>>> import fileparse
>>> camion = fileparse.parse_csv('../Data/camion.csv', types=[str,int,float])
>>>
Actualmente la función solicita el nombre de un archivo, pero podés hacer el código más flexible. Modificá la función de modo que funcione con cualquier objeto o iterable que se comporte como un archivo. Por ejemplo:

>>> import fileparse
>>> import gzip
>>> with gzip.open('../Data/camion.csv.gz', 'rt') as file:
...      camion = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
>>> camion = fileparse.parse_csv(lines, types=[str,int,float], has_headers = False)
>>>
Y ahora que pasa si le pasás un nombre de archivo como antes ?

>>> camion = fileparse.parse_csv('../Data/camion.csv', types=[str,int,float])
>>> camion
... mirá la salida (debería ser un lío) ...
>>>
Sí, hay que tener cuidado.
"""

import fileparse
import gzip
with gzip.open('Data/camion.csv.gz', 'rt') as file:
    camion = fileparse.parse_csv("Data/camion.csv", types=[str, int, float], 
                             has_headers=True)

