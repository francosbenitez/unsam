"""
Ejercicio 7.2: Función main()
Usando estas ideas, agregá a tu programa informe.py una función main() que tome una lista de parámetros en la línea de comandos y produzca la misma salida que antes.

bash % python3 informe.py Data/camion.csv Data/precios.csv
También deberías poder ejecutarlo del siguiente modo dentro del intérprete interactivo de Python:

>>> import informe
>>> informe.main(['informe.py', '../Data/camion.csv', '../Data/precios.csv'])

    Nombre    Cajones     Precio     Cambio
 ---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84

>>>
Análogamente, modificá el archivo costo_camion.py para que incluya una función similar main() que te permita hacer esto:

>>> import costo_camion
>>> costo_camion.main(['costo_camion.py', '../Data/camion.csv'])
Total cost: 47671.15
>>>
"""

import csv

def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        contenido_camion = []
        for n_row, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                contenido_camion.append({'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])})
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return contenido_camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        lista_precios = {}
        for n_row, row in enumerate(rows, start = 1):
            try:
                nombre = row[0]
                try:
                    precio = float(row[1])
                except:
                    print(f'el precio de la fila {n_row} es invalido.')
            except:
                print(f'nombre vacio en la fila {n_row}')
            lista_precios[nombre] = precio
        return lista_precios
    
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

def main(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion) 
    precios = leer_precios(nombre_archivo_precios) 
    informe = hacer_informe(camion, precios) 
    imprimir_informe(informe) 

if __name__ == "__main__":
    main('Data/camion.csv', 'Data/precios.csv')
