"""
Ejercicio 7.5: Arreglemos las funciones existentes
Arreglá las funciones leer_camion() y leer_precios() en el archivo informe.py de modo que funcionen con la nueva versión de parse_csv(). Con una pequeña modificación es suficiente. Después de esto tus programas informe.py y costo_camion.py deberían funcionar tan bien como antes.

Por ahora dejamos estos archivos y pasamos a otras discusiones. Dejá estos archivos listos para entregar al final de la clase.
"""

# import csv
import fileparse

def leer_camion(nombre_archivo):
    return fileparse.parse_csv('Data/camion.csv', types = [str, int, float], 
                   has_headers=True, silence_errors = True)

def leer_precios(nombre_archivo):
    return fileparse.parse_csv('Data/precios.csv', types = [str, float], 
                   has_headers=False)
    
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



