"""
Ejercicio 2.8: Administración de errores
Probá correr la siguiente función ingresando tu edad real, una edad escrita con letras (como "ocho") y una edad negativa (-3):

def preguntar_edad(nombre):
   edad = int(input(f'ingresá tu edad {nombre}: '))
   if edad<0:
       raise ValueError('La edad no puede ser negativa.')
   return edad
Ahora probá este ejemplo que atrapa la excepción generada con raise y continúa la ejecución con la siguiente persona.

for nombre in ['Pedro','Juan','Caballero']:
   try:
       edad = preguntar_edad(nombre)
       print(f'{nombre} tiene {edad} años.')
   except ValueError:
       print(f'{nombre} no ingresó una edad válida.')
Vamos a usar estas ideas aplicadas al procesamiento de un archivo CSV. ¿Qué pasa si intentás usar la función costo_camion() con un archivo que tiene datos faltantes?

>>> costo_camion('Data/missing.csv')
Traceback (most recent call last):
   File "<stdin>", line 1, in <módulo>
   File "costo_camion.py", line 11, in costo_camion
   ncajones = int(fields[1])
ValueError: invalid literal for int() with base 10: ''
>>>
El programa termina con un error. A esta altura tenés que tomar una decisión. Para que el programa funcione podés editar el archivo CSV de entrada de manera de corregirlo (borrando líneas o adecuando la información) o podés modificar el código para que maneje las líneas incorrectas de alguna manera.

Modificá el programa costo_camion.py para que atrape la excepción con un bloque try - except, imprima un mensaje de aviso (warning) y continúe procesando el resto del archivo.

Vamos a profundizar en la administración de errores en las próximas clases.
"""

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    i = 0
    costo = 0
    for row in rows:
        try:
            cajones = int(row[1])
            precio = float(row[2])
            costo += cajones * precio
            i = i + 1 
        except ValueError:
            print("Warning!")
    return costo
    
costo = costo_camion("Data/missing.csv")
print("Costo total:", costo)


