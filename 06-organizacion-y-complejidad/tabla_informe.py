import csv
​
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
​
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
                    print(f'el precio de la fila {n_row} es inválido.')
            except:
                print(f'nombre vacío en la fila {n_row}')
            lista_precios[nombre] = precio
        return lista_precios
    
def hacer_informe(carga,precios):
    informe = []
    for registro in carga:
        cambio = precios[registro['nombre']]-registro['precio']
        tupla = (registro['nombre'],registro['cajones'],registro['precio'],cambio)
        informe.append(tupla)
    return informe
​
​
camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
   
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 + ' ') * len(headers))
for row in informe:
    print('%10s %10d %10.2f %10.2f' % row)