"""
Ejercicio 6.4: Estructurar un programa como una colección de funciones
Volvé a tu programa tabla_informe.py y modificalo de modo que todas las operaciones principales, incluyendo cálculos e impresión, sean llevados a cabo por una colección de funciones. Guarda la nueva versión en un archivo informe_funciones.py. Más específicamente:

Creá una función imprimir_informe(informe) que imprima el informe.
Cambiá la última parte del programa de modo que consista sólo en una serie de llamados a funciones, sin ningún cómputo.

Ejercicio 6.5: Crear una función de alto nivel para la ejecución del programa.
Juntá la última parte de tu programa en una única función informe_camion(nombre_archivo_camion, nombre_archivo_precios). Deberías obtener una función que al llamarla como sigue, imprima el informe:

informe_camion('../Data/camion.csv', '../Data/precios.csv')
En su versión final tu programa será una serie de definiciones de funciones seguidos por un único llamado a la funcion informe_camion() (la cual ejecuta todos los pasos que constituyen tu programa).

Cuando tu programa es una única función, es muy simple ejecutarlo con diferentes entradas. Por ejemplo, después de ejecutar tu programa probá estos comandos en modo interactivo:

>>> informe_camion('../Data/camion2.csv', '../Data/precios.csv')
... mirá el resultado ...

>>> files = ['../Data/camion.csv', '../Data/camion2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()

... mirá el resultado ...
>>>
"""

import csv

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        contenido_camion = []
        for n_row, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                contenido_camion.append({'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])})
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return contenido_camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        lista_precios = {}
        for n_row, row in enumerate(rows, start = 1):
            try:
                nombre = row[0]
                try:
                    precio = float(row[1])
                except:
                    print(f'el precio de la fila {n_row} es invalido.')
            except:
                print(f'nombre vacio en la fila {n_row}')
            lista_precios[nombre] = precio
        return lista_precios
    
def hacer_informe(carga,precios):
    informe = []
    for registro in carga:
        cambio = precios[registro['nombre']]-registro['precio']
        tupla = (registro['nombre'],registro['cajones'],registro['precio'],cambio)
        informe.append(tupla)
    return informe

def imprimir_informe(informe):
    camion = leer_camion('Data/camion.csv')
    precios = leer_precios('Data/precios.csv')
    informe = hacer_informe(camion, precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion) 
    precios = leer_precios(nombre_archivo_precios) 
    informe = hacer_informe(camion, precios) 
    imprimir_informe(informe) 

informe_camion('Data/camion.csv', 'Data/precios.csv')


