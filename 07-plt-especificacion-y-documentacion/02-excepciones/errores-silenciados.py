"""
Ejercicio 7.1: Errores silenciados
Modificá parse_csv() de modo que le usuarie pueda silenciar los informes de errores en el parseo de los datos que agregaste antes.Por ejemplo:

>>> camion = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors = True)
>>> camion
[{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
 {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
 {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
 {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
 {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1}]
>>>
"""

import csv

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