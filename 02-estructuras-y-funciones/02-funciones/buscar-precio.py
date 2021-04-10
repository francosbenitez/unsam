"""
Ejercicio 2.7: Buscar precios
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura) y lo imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.

>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.
Guardá este código en un archivo buscar_precio.py para entregar al final de la clase.
"""

def buscar_precio(fruta_buscada):
    f = open("Data/precios.csv", "rt")
    precio = 0
    for line in f:
        row = line.strip('\n').split(',')
        fruta = row[0]
        precio_fruta = row[-1]
        if fruta == fruta_buscada:
                precio = precio_fruta
    if precio == 0:
        return f"{fruta_buscada} no figura en la lista de precios."
    else:
        return f"El precio de un cajón de {fruta_buscada} es: {precio}."

precio = buscar_precio("Kale")
print(precio)
