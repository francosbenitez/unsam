"""
Ejercicio 4.17: Fijando ideas
Usando las técnicas de este ejercicio, vas a poder escribir instrucciones que conviertan fácilmente campos como los de nuestro archivo en un diccionario de Python.

Para ilustrar esto, supongamos que leés un archivo de datos de la siguiente forma:

>>> f = open('../Data/dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
Convirtamos estos datos usando un truco similar:

>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
Bonus: ¿Cómo modificarías este ejemplo para transformar la fecha (date) en una tupla como (6, 11, 2007)?

Es importante que entiendas lo que hicimos en este ejercicio. Volveremos sobre esto más adelante.
"""

import csv

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
record["date"] = (int(record["date"][0]), int(record["date"][2:4]), int(record["date"][5:]))
converted = [tuple([int(a) for a in func(val).split('/')])
             if func==str and len(func(val).split('/'))==3 else func(val)
             for func, val in zip(types, row)]





