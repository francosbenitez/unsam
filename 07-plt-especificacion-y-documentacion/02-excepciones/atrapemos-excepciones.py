"""
Atrapemos excepciones
La función parse_csv() que escribiste está destinada a procesar un archivo completo. Pero en una situacion real, es posible que los archivos CSV de entrada estén "rotos", ausentes, o que su contenido no se adecúe al formato esperado. Probá esto:

>>> camion = parse_csv('../Data/missing.csv', types = [str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
El error es: el texto '' es inválido para la función int()

Modificá la función parse_csv() de modo que atrape todas las excepciones de tipo ValueError generadas durante el armado de los registros a devolver e imprima un mensaje de advertencia para las filas que no pudieron ser convertidas. Estas filas no deben ser procesadas (ya que no se puede hacer adecuadamente), y deben ser omitidas en el output de la función.

Este mensaje deberá incluir el número de fila que causó el problema y el motivo por el cual falló la conversión. Para probar tu nueva función, intentá procesar Data/missing.csv. Debería darte algo así:

>>> camion = parse_csv('../Data/missing.csv', types = [str, int, float])
Fila 4: No pude convertir ['Mandarina', '', '51.23']
Fila 4: Motivo: invalid literal for int() with base 10: ''
Fila 7: No pude convertir ['Naranja', '', '70.44']
Fila 7: Motivo: invalid literal for int() with base 10: ''
>>>
>>> camion
[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1}]
>>>
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        try:
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
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    if not row:    
                        continue
                    if indices:
                        row = [row[index] for index in indices]
                    registro = dict(zip(headers, row))
                    registros.append(registro)
            else: 
                registros = {}
                for row in rows:
                    if types:
                        row = [func(val) for func, val in zip(types, row)]
                    if not row:   
                        continue
                    registros[row[0]] = row[1]
        except ValueError:
            print(f"Fila {i}: No pude convertir {row}")
    return registros

camion = parse_csv('Data/missing.csv', types = [str, int, float], 
                   has_headers=True)
