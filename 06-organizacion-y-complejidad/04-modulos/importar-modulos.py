"""
Ejercicio 6.10: Importar módulos
En el Ejercicio 6.6 creamos una función llamada parse_csv() para parsear el contenido de archivos de datos en formato CSV. Ahora vamos a ver cómo usar esa función en otros programas.

Empezá por copiarte los archivos rebotes.py, hipoteca.py, informe.py y fileparse.py a la carpeta de ejercicios de esta clase. Los vamos a importar.

Con el directorio de trabajo adecuado (puede que tengas que reiniciar tu intérprete para que tome efecto un cambio), intentá importar los programas que escribiste antes. Con sólo importarlos deberías ver su salida exactamente como cuando los terminaste de escribir.

Repetimos: al importar un módulo ejecutás su código.

>>> import rebotes
#... mirá la salida ...
>>> import hipoteca
#... mirá la salida ...
>>> import informe
#... mirá la salida ...
>>>
Si nada de esto funciona, es probable que estés ejecutando Python desde la carpeta equivocada.

Ahora probá importar tu módulo fileparse y pedile help.

>>> import fileparse
>>> help(fileparse)
... mirá la salida ...
>>> dir(fileparse)
... mirá la salida ...
>>>
Intentá usar el módulo para leer datos de un archivo:

>>> camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
>>> camion
... mirá la salida ...
>>> lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
>>> lista_precios
... mirá la salida ...
>>> precios = dict(lista_precios)
>>> precios
... fijate la salida ...
>>> precios['Naranja']
106.28
>>>
Importá sólo la función para evitar escribir el nombre del módulo:

>>> from fileparse import parse_csv
>>> camion = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
>>> camion
... fijate la salida ...
>>>
"""

import rebotes
import tablas
import tabla_informe
import conversion

camion = conversion.parse_csv('Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])

from conversion import parse_csv
camion = parse_csv('Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
