"""
Ejercicio 6.11: Usemos tu módulo
En el Ejercicio 6.4 escribiste un programa informe_funciones.py que produce un informe como éste:

    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100     $32.20       8.02
   Naranja         50     $91.10      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50     $65.10      15.79
   Naranja        100     $70.44      35.84
Retomá ese programa (si lo perdiste, te dejamos una versión para que la leas y la puedas usar) y modificalo de modo que todo el procesamiento de archivos de entrada de datos se haga usando funciones del módulo fileparse. Para lograr éso, importá fileparse como un módulo y cambiá las funciones leer_camion() y leer_precios() para que usen la función parse_csv() .

Guiate por el ejemplo interactivo que dimos un poco más arriba. Al final, deberías obtener exactamente el mismo resultado que al principio.
"""

from trabajando import parse_csv

def leer_camion(nombre_archivo):
    return parse_csv('Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)

def leer_precios(nombre_archivo):
    return parse_csv('Data/precios.csv', types=[str, float], has_headers = False)
    
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





