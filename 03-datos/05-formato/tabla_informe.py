"""
Ejercicio 3.13: Recolectar datos
En el Ejercicio 2.18, escribiste un programa llamado informe.py que calculaba las ganancias o pérdidas de un camión que compra a productores y vende en el mercado. Dejá ese archivo para entregar al final de la clase y copiá su contenido en un archivo tabla_informe.py. En este ejercicio, vas a comenzar a modificarlo para producir una tabla como ésta:

 Nombre     Cajones     Precio     Cambio
---------- ---------- ---------- ----------
 Lima          100        32.2       8.02
 Naranja        50        91.1      15.18
 Caqui         150      103.44       2.02
 Mandarina     200       51.23      29.66
 Durazno        95       40.37      33.11
 Mandarina      50        65.1      15.79
 Naranja       100       70.44      35.84
En este informe, el "Precio" es el precio en el mercado y el "Cambio" es la variación respecto al precio cobrado por el productor.

Para generar un informe como el de arriba, primero tenés que recolectar todos los datos de la tabla. Escribí una función hacer_informe() que recibe una lista de cajones y un diccionario con precios como input y devuelve una lista de tuplas conteniendo la información mostrada en la tabla anterior.

Agregá esta función a tu archivo tabla_informe.py. Debería funcionar como se muestra en el siguiente ejemplo:

>>> camion = leer_camion('../Data/camion.csv')
>>> precios = leer_precios('../Data/precios.csv')
>>> informe = hacer_informe(camion, precios)
>>> for r in informe:
        print(r)

('Lima', 100, 32.2, 8.019999999999996)
('Naranja', 50, 91.1, 15.180000000000007)
('Caqui', 150, 103.44, 2.019999999999996)
('Mandarina', 200, 51.23, 29.660000000000004)
('Durazno', 95, 40.37, 33.11000000000001)
('Mandarina', 50, 65.1, 15.790000000000006)
('Naranja', 100, 70.44, 35.84)
...
>>>
Ejercicio 3.14: Imprimir una tabla con formato
Volvé a hacer el ciclo for del ejercicio anterior pero cambiando la forma de imprimir como sigue:

>>> for r in informe:
        print('%10s %10d %10.2f %10.2f' % r)

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
O directamente usando f-strings. Por ejemplo:

>>> for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
...
>>>
Agregá estos últimos comandos a tu programa tabla_informe.py. Hacé que el programa tome la salida de la función hacer_informe() e imprima una tabla bien formateada.

Ejercicio 3.15: Agregar encabezados
Suponete que tenés una tupla con nombres de encabezado como ésta:

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
Agregá el código necesario a tu programa para que tome una tupla de encabezados como la de arriba y cree una cadena donde cada nombre de encabezado esté alineado a la derecha en un campo de 10 caracteres de ancho y separados por un solo espacio.

'    Nombre    Cajones     Precio     Cambio'
Escribí el código que recibe los encabezados y crea una cadena de separación entre los encabezados y los datos que siguen. Esta cadena es simplemente una tira de caracteres "-" bajo cada nombre de campo. Por ejemplo:

'---------- ---------- ---------- ----------'
Cuando esté listo, tu programa debería producir una tabla como esta:

    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      32.20       8.02
   Naranja         50      91.10      15.18
     Caqui        150     103.44       2.02
 Mandarina        200      51.23      29.66
   Durazno         95      40.37      33.11
 Mandarina         50      65.10      15.79
   Naranja        100      70.44      35.84
Ejercicio 3.16: Un desafío de formato
Por último, modificá tu código para que el precio mostrado incluya un símbolo de pesos ($) y la salida se vea como esta tabla:

    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
Guardá estos cambios en el archivo tabla_informe.py que más adelante los vas a necesitar.
"""

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = list()
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        camion.append(lote)
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

def hacer_informe(camion, precios):
    cambio = []
    for carga in camion:
        for precio in precios:
            # si los nombres son iguales
            if precio == carga["nombre"]:
                resta = (
                    # agrega nombre, cajon y precio
                    carga["nombre"],
                    int(carga["cajones"]),
                    round(float(carga["precio"]), 2),
                    # agrega el cambio 
                    round(float(precios[precio]) - float(carga["precio"]), 2)
                        )
                cambio.append(resta)
    return cambio

precios = leer_precios("Data/precios.csv")
camion = leer_camion("Data/camion.csv")
informe = hacer_informe(camion, precios)

headers = ("Nombre", "Cajones", "Precio", "Cambio")
print(f'{headers[0]:^10s} {headers[1]:^10s} {headers[2]:^10s} {headers[3]:^10s}')
print("---------- ---------- ---------- ----------")
for row in informe:
    row = (row[0], row[1], '$'+str(row[2]), row[3])
    print(f'{row[0]:^10s} {row[1]:^10d} {row[2]:^10s} {row[3]:^10.2f}')

costo_camion = costo_camion("Data/camion.csv")
recaudacion = 0
for producto in camion:
    nombre = float(buscar_precio(producto["nombre"]))
    cajones = int(producto["cajones"])
    recaudacion += nombre * cajones

diferencia = recaudacion - costo_camion
mensaje = f"\nCosto del camion: {costo_camion} | Recaudacion: {recaudacion} | Ganancia: {diferencia:.2f}"
print(mensaje)