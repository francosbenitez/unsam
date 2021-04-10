"""
Ejercicio 2.17: Diccionarios como contenedores
Los diccionarios son útiles si querés buscar elementos usando índices que no sean números enteros. En la terminal de Python, jugá con un diccionario:

>>> precios = {}
>>> precios['Naranja'] = 92.45
>>> precios['Mandarina'] = 45.12
>>> precios
... mirá el resultado ...
>>> precios['Naranja']
92.45
>>> precios['Manzana']
... mirá el resultado ...
>>> 'Manzana' in precios
False
>>>
En el Ejercicio 2.7 escribiste una función que busca el precio de una determinada fruta o verdura en el archivo ../Data/precios.csv. Esto es útil para saber sobre un producto en particular, pero si necesitás tener los precios de toda la mercadería, no resulta práctico abrir y cerrar el archivo para consultar cada precio. Por eso ahora te proponemos generar un diccionario que contenga todos los precios. En este diccionario, podés consultar luego los precios de cada producto.

Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios como éste arme un diccionario donde las claves sean los nombres de frutas y verduras, y los valores sean los precios por cajón.

Para hacerlo, empezá con un diccionario vacío y andá agregándole valores igual a como hiciste antes, pero ahora esos valores los vas leyendo del archivo.

Vamos a usar esta estructura de datos para buscar rápidamente los precios de las frutas y verduras.

Un par de consejos: Usá el módulo csv igual que antes.

>>> import csv
>>> f = open('../Data/precios.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
       print(row)


['Lima', '40.22']
['Uva', '24.85']
...
[]
>>>
El archivo Data/precios.csv puede tener líneas en blanco, esto te puede traer complicaciones. Observá que arriba figura una lista vacía (la última), porque la última línea del archivo no tenía datos.

Puede suceder que esto haga que tu programa termine con una excepción. Usá los comandos try y except para evitar el problema. Para pensar: ¿Sería mejor prevenir estos problemas con el comando if en vez de try y except?

Una vez que hayas escrito tu función leer_precios(), testeala interactivamente para asegurarte de que funciona bien:

>>> precios = leer_precios('../Data/precios.csv')
>>> precios['Naranja']
106.28
>>> precios['Mandarina']
80.89
>>>
"""

import csv 

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
        
precios = leer_precios("Data/precios.csv")
print(precios)
