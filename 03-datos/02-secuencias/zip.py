"""
Ejercicio 3.4: La función zip()
En el archivo Data/camion.csv, la primera línea tiene los encabezados de las columnas. En los códigos anteriores la descartamos.

>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> encabezados = next(filas)
>>> encabezados
['nombre', 'cajones', 'precio']
>>>
Pero, ¿no puede ser útil conocer los encabezados? Es acá donde la función zip() entra en acción. Primero tratá de aparear los encabezados con una fila de datos:

>>> fila = next(filas)
>>> fila
['Lima', '100', '32.20']
>>> list(zip(encabezados, fila))
[ ('nombre', 'Lima'), ('cajones', '100'), ('precio', '32.20') ]
>>>
Fijate cómo zip() apareó los encabezados de las columnas con los valores de la columna. Usamos list() arriba para devolver el resultado en una lista de forma que lo puedas ver. Normalmente, zip() crea un iterador que debe ser consumido en un ciclo for.

Este apareamiento es un paso intermedio para construir un diccionario. Probá lo siguiente:

>>> record = dict(zip(encabezados, fila))
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
Esta transformación es un truco sumamente útil cuando tenés que procesar muchos archivos de datos. Por ejemplo, suponé que querés hacer que el programa costo_camion.py trabaje con diferentes archivos de entrada, pero que no le importe la posición exacta de la columna que tiene la cantidad de cajones o el precio. Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posición dentro del archivo.

Modificá la función costo_camion() en el archivo costo_camion.py para que se vea así:

# costo_camion.py

def costo_camion(nombre_archivo):
    ...
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        ...
Ahora, probá tu función con un archivo completamente diferente Data/fecha_camion.csv que se ve así:

nombre,fecha,hora,cajones,precio
"Lima","6/11/2007","9:50am",100,32.20
"Naranja","5/13/2007","4:20pm",50,91.10
"Caqui","9/23/2006","1:30pm",150,83.44
"Mandarina","5/17/2007","10:30am",200,51.23
"Durazno","2/1/2006","10:45am",95,40.37
"Mandarina","10/31/2006","12:05pm",50,65.10
"Naranja","7/9/2006","3:15pm",100,70.44
>>> costo_camion('../Data/fecha_camion.csv')
47671.15
>>>
Si lo hiciste bien, vas a descubrir que tu programa aún funciona a pesar de que le pasaste un archivo con un formato de columnas completamente diferente al de antes. ¡Y eso está muy bueno!

El cambio que hicimos acá es sutil, pero importante. En lugar de tener hardcodeado un formato fijo, la nueva versión de la función costo_camion() puede sacar la información de interés de cualquier archivo CSV. En la medida en que el archivo tenga las columnas requeridas, el código va a funcionar.

Modificá el programa informe.py que escribiste antes (ver Ejercicio 2.18) para que use esta técnica para elegir las columnas a partir de sus encabezados.

Probá correr el programa informe.py sobre el archivo Data/fecha_camion.csv y fijate si da la misma salida que antes.
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo = 0
    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            cajones = int(record["cajones"])
            precio = float(record["precio"])
            costo += cajones * precio
        except ValueError:
            print(f"Fila {n_row}: No pude interpretar. {row}")
    return costo
    
costo = costo_camion("Data/fecha_camion.csv")
print("Costo total:", costo)
