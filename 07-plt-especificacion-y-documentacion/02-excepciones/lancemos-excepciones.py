"""
Lancemos excepciones
La función parse_csv() que escribiste en el Ejercicio 6.9 admite seleccionar algunas columnas por le usuarie, pero eso sólo funciona si el archivo de entrada tiene encabezados.

Modifcá tu código para que lance una excepción en caso que ambos parámetros select y has_headers = False sean pasados juntos. Y que resulte:

>>> parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("Para seleccionar, necesito encabezados.")
RuntimeError: Para seleccionar, necesito encabezados.
>>>
Ahora que agregaste este control, te estarás preguntando si no deberías comprobar otras cosas también en tu función. Por ejemplo, ¿deberías comprobar que nombre_archivo sea una cadena, que tipos sea una lista y otras cosas de ese estilo?

Como regla general, es mejor no controlar esas cosas, y dejar que el programa dé un error ante entradas inválidas. El mensaje de error va a darte una idea del origen del problema y te va ayudar a solucionarlo.

El motivo principal para agregar controles de calidad sobre los parámetros de entrada es evitar que tu programa sea ejecutado en condiciones que no tienen sentido. Si le pedís que haga algo que requiere encabezados y simultáneamente le decís que no existen encabezados implica estás usando la función incorrectamente. La idea general es estar protegido contra situaciones que "no deberían suceder" pero podrían.
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        if (select != None) and (has_headers == False):
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        rows = csv.reader(f)
        if has_headers == True:
            headers = next(rows)
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
            registros = []
            for row in rows:
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
    return registros

parse_csv('Data/precios.csv', select = ['nombre','precio'], has_headers = False)
