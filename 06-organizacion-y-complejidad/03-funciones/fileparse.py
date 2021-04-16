"""
Ejercicio 6.6: Parsear un archivo CSV
Vamos a empezar por el problema simple de leer un archivo CSV para guardar los datos que contiene en una lista de diccionarios. En el archivo fileparse.py definí la siguiente función:

# fileparse.py
import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros
Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV. La función aísla al programador de los múltiples pequeños pasos necesarios para abrir un archivo, "envolverlo" con el módulo csv, ignorar líneas vacías, y demás minucias.

(un "wrapper" (envoltorio) en programación es una estructura que expone la interfase de un objeto, pero aísla al usuario de los detalles de funcionamiento de ese objeto.)

Probémoslo en tu IDE o con python3 -i fileparse.py.

>>> camion = parse_csv('../Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': '100', 'precio': '32.2'}, {'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}, {'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}, {'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}, {'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}, {'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}, {'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}]
>>>
La función hace lo que queríamos, pero no podemos usar los resultados para hacer cálculos porque todos los datos recuperados son de tipo cadena (string). Ya vamos a solucionar esto. Por ahora sigamos extendiendo sus funciones.

Ejercicio 6.7: Selector de Columnas
La mayoría de los casos, uno no está interesado en todos los datos que contiene el archivo CSV, sino sólo en algunas columnas. Modifiquemos la función parse_csv de modo que permita al usuario elegir (opcionalmente) algunas columnas del siguiente modo:

>>> # Lee todos los datos
>>> camion = parse_csv('../Data/camion.csv')
>>> camion
[{'nombre': 'Lima', 'cajones': '100', 'precio': '32.2'}, {'nombre': 'Naranja', 'cajones': '50', 'precio': '91.1'}, {'nombre': 'Caqui', 'cajones': '150', 'precio': '103.44'}, {'nombre': 'Mandarina', 'cajones': '200', 'precio': '51.23'}, {'nombre': 'Durazno', 'cajones': '95', 'precio': '40.37'}, {'nombre': 'Mandarina', 'cajones': '50', 'precio': '65.1'}, {'nombre': 'Naranja', 'cajones': '100', 'precio': '70.44'}]

>>> # Lee solo algunos datos
>>> cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])
>>> cajones_retenidos
[{'nombre': 'Lima', 'cajones': '100'}, {'nombre': 'Naranja', 'cajones': '50'}, {'nombre': 'Caqui', 'cajones': '150'}, {'nombre': 'Mandarina', 'cajones': '200'}, {'nombre': 'Durazno', 'cajones': '95'}, {'nombre': 'Mandarina', 'cajones': '50'}, {'nombre': 'Naranja', 'cajones': '100'}]
>>>
Vimos un ejemplo de un selector de columnas en el Ejercicio 4.11. De todos modos, ésta es otra forma de resolverlo:

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
Esta parte es un toque técnica y merece una mirada de más cerca. El paso más delicado es traducir los nombres de las columnas seleccionadas a índices. Por ejemplo, supongamos que los encabezados en el archivo de entrada fueran los siguientes:

>>> encabezados = ['nombre', 'dia', 'hora', 'cajones', 'precio']
>>>
Y que las columnas seleccionadas fueran:

>>> select = ['nombre', 'cajones']
>>>
Para hacer la selección correctamente, tenés que conventir los nombres de las columnas listadas en select a índices (posiciones) de columnas en el archivo. Esto es exactamente lo que hace este paso:

>>> indices = [encabezados.index(nombre_columna) for nombre_columna in select ]
>>> indices
[0, 3]
>>>
En otras palabras, "nombre" es la columna 0 y "cajones" es la columna 3. Al leer una línea de datos del archivo, usás los índices para filtrarla y rescatar sólo las columnas que te interesan:

>>> linea = ['Lima', '6/11/2007', '9:50am', '100', '32.20' ]
>>> linea = [ linea[indice] for indice in indices ]
>>> linea
['Lima', '100']
>>>
"""

import csv

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

camion = parse_csv('Data/camion.csv')

def parse_csv(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila: 
                continue
            if indices:
                fila = [fila[index] for index in indices]
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    return registros

cajones_retenidos = parse_csv('Data/camion.csv', select=['nombre','cajones'])
