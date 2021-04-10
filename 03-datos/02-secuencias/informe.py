"""
Ejercicio 3.4: La funci�n zip()
En el archivo Data/camion.csv, la primera l�nea tiene los encabezados de las columnas. En los c�digos anteriores la descartamos.

>>> f = open('../Data/camion.csv')
>>> filas = csv.reader(f)
>>> encabezados = next(filas)
>>> encabezados
['nombre', 'cajones', 'precio']
>>>
Pero, �no puede ser �til conocer los encabezados? Es ac� donde la funci�n zip() entra en acci�n. Primero trat� de aparear los encabezados con una fila de datos:

>>> fila = next(filas)
>>> fila
['Lima', '100', '32.20']
>>> list(zip(encabezados, fila))
[ ('nombre', 'Lima'), ('cajones', '100'), ('precio', '32.20') ]
>>>
Fijate c�mo zip() apare� los encabezados de las columnas con los valores de la columna. Usamos list() arriba para devolver el resultado en una lista de forma que lo puedas ver. Normalmente, zip() crea un iterador que debe ser consumido en un ciclo for.

Este apareamiento es un paso intermedio para construir un diccionario. Prob� lo siguiente:

>>> record = dict(zip(encabezados, fila))
>>> record
{'precio': '32.20', 'nombre': 'Lima', 'cajones': '100'}
>>>
Esta transformaci�n es un truco sumamente �til cuando ten�s que procesar muchos archivos de datos. Por ejemplo, supon� que quer�s hacer que el programa costo_camion.py trabaje con diferentes archivos de entrada, pero que no le importe la posici�n exacta de la columna que tiene la cantidad de cajones o el precio. Es decir, que entienda que la columna tiene el precio por su encabezado y no por su posici�n dentro del archivo.

Modific� la funci�n costo_camion() en el archivo costo_camion.py para que se vea as�:

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
Ahora, prob� tu funci�n con un archivo completamente diferente Data/fecha_camion.csv que se ve as�:

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
Si lo hiciste bien, vas a descubrir que tu programa a�n funciona a pesar de que le pasaste un archivo con un formato de columnas completamente diferente al de antes. �Y eso est� muy bueno!

El cambio que hicimos ac� es sutil, pero importante. En lugar de tener hardcodeado un formato fijo, la nueva versi�n de la funci�n costo_camion() puede sacar la informaci�n de inter�s de cualquier archivo CSV. En la medida en que el archivo tenga las columnas requeridas, el c�digo va a funcionar.

Modific� el programa informe.py que escribiste antes (ver Ejercicio 2.18) para que use esta t�cnica para elegir las columnas a partir de sus encabezados.

Prob� correr el programa informe.py sobre el archivo Data/fecha_camion.csv y fijate si da la misma salida que antes.
"""

import csv

def leer_camion(nombre_archivo):
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
        for row in camion:
            row["cajones"] = int(row["cajones"])
            row["precio"] = float(row["precio"])
    return camion

def leer_precios(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    diccionario = {}
    for row in rows:
        try:  
            fruta = row[0]
            precio = float(row[1])
            diccionario[fruta] = precio
        except:
            continue
    return diccionario

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

def buscar_precio(fruta_buscada):
    f = open("Data/precios.csv", "rt")
    precio = 0
    for line in f:
        row = line.strip('\n').split(',')
        fruta = row[0]
        precio_fruta = row[-1]
        if fruta == fruta_buscada:
                precio = precio_fruta
    return float(precio)

camion = leer_camion("Data/camion.csv")
costo_camion = costo_camion("Data/camion.csv")
recaudacion = 0
for producto in camion:
    nombre = float(buscar_precio(producto["nombre"]))
    cajones = int(producto["cajones"])
    recaudacion += nombre * cajones

diferencia = recaudacion - costo_camion
mensaje = f"Costo del camion: {costo_camion} | Recaudacion: {recaudacion} | Ganancia: {diferencia:.2f}"
print(mensaje)










