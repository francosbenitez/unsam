"""
Ejercicio 6.9: Trabajando sin encabezados
Algunos archivos CSV no tiene información de los encabezados. Por ejemplo, el archivo precios.csv se ve así:

Lima,40.22
Uva,24.85
Ciruela,44.85
Cereza,11.27
...
Modificá la función parse_csv() de forma que (opcionalmente) pueda trabajar con este tipo de archivos, creando tuplas en lugar de diccionarios cuando no haya encabezados. Por ejemplo:

>>> precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
>>> precios
[(Lima,40.22), (Uva,24.85), (Ciruela,44.85), (Cereza,11.27), (Frutilla,53.72), (Caqui,105.46), (Tomate,66.67), (Berenjena,28.47), (Lechuga,24.22), (Durazno,73.48), (Remolacha,20.75), (Habas,23.16), (Frambuesa,34.35), (Naranja,106.28), (Bruselas,15.72), (Batata,55.16), (Rúcula,36.9), (Radicheta,26.11), (Repollo,49.16), (Cebolla,58.99), (Cebollín,57.1), (Puerro,27.58), (Mandarina,80.89), (Ajo,15.19), (Rabanito,51.94), (Zapallo,24.79), (Espinaca,52.61), (Acelga,29.26), (Zanahoria,49.74), (Papa,69.35)]
>>>
Para hacer este cambio, vas a tener que modificar el código de forma que, si le pasás el parámetro has_headers = False, la primera línea de datos no sea interpretada como encabezado. Además, en ese caso, vas a tener que asegurarte de no crear diccionarios, dado que no tenés más los nombres de las columnas para usar en el encabezado. Vale aclarar que este parámetro debe tener como valor por omisión True, con lo que la función sigue funcionando igual que antes si no se especifica has_headers = False.

Si bien no es difícil, este es un cambio muy grande en esta función. Un camino posible es poner un if has_headers al principio y resolver cada caso por separado. Otro camino es poner condicionales en cada paso donde sea necesario operar de manera diferente.

Incorporá todos estos cambios en el archivo fileparse.py.
"""

import csv

def parse_csv(nombre_archivo, types = None, has_headers = None):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        registros = []
        if has_headers == True:
            headers = next(rows)
            for row in rows:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if not row:    
                    continue
            registro = dict(zip(headers, row))
            registros.append(registro)
        else: 
            for row in rows:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if not row:    
                    continue
                lote = (row[0], row[1])
                registros.append(lote)
    return registros

precios = parse_csv('Data/precios.csv', types=[str, float], has_headers = False)