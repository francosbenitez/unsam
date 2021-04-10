"""
Ejercicio 2.2: Lectura de un archivo de datos
Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple con los datos leídos.

Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo como punto flotante, usá float(s).

Tu programa debería imprimir una salida como la siguiente:

Costo total 47671.15
Acordate de guardar tu archivo en el directorio Clase02; vamos a volver a trabajar sobre él.
"""

f = open("Data/camion.csv", "rt")
headers = next(f)
costo = 0

for line in f:
    row = line.split(',')
    cajones = int(row[1])   
    precio = float(row[2])  
    costo += cajones * precio  
    
print("Costo total", costo)