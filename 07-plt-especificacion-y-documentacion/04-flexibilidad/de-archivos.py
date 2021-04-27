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

import csv
import gzip

def parse_csv(nombre_archivo, select = None, types = None, 
              has_headers = None, 
              silence_errors = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
            rows = csv.reader(f)
            if has_headers == True:
                headers = next(rows)
                if select:
                    indices = [headers.index(nombre_columna) for nombre_columna in select]
                    headers = select
                else:
                    indices = []
                registros = []
                for i, row in enumerate(rows):
                    if silence_errors == True: 
                        try:
                            if types:
                                row = [func(val) for func, val in zip(types, row)]
                            if not row:    
                                continue
                            if indices:
                                row = [row[index] for index in indices]
                            registro = dict(zip(headers, row))
                            registros.append(registro)
                        except ValueError:
                            pass
                    else:
                        try:
                            if types:
                                row = [func(val) for func, val in zip(types, row)]
                            if not row:    
                                continue
                            if indices:
                                row = [row[index] for index in indices]
                            registro = dict(zip(headers, row))
                        except ValueError as error:
                            print(f"Fila {i}: No pude convertir {row}")
                            print(f"Fila {i}: Motivo:", error)
                        registros.append(registro)
            else: 
                registros = {}
                for row in rows:
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    if not row:   
                        continue
                    registros[row[0]] = row[1]
        
    return registros

camion = parse_csv('Data/missing.csv', types = [str, int, float], 
                   has_headers=True, silence_errors = True)

with gzip.open('Data/camion.csv.gz', 'rt') as file:
    camion = parse_csv(file, types = [str,int,float], silence_errors = True)
    
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion = fileparse.parse_csv(lines, types=[str,int,float], has_headers = False)

