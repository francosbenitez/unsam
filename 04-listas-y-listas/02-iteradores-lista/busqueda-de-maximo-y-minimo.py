"""
Ejercicio 4.7: Búsqueda de máximo y mínimo
Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque el valor máximo de una lista de números positivos. Python tiene el comando max que ya hace esto, pero como práctica te proponemos que completes el siguiente código:

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        ...
    return m
Probá tu función con estos ejemplos:

>>> maximo([1,2,7,2,3,4])
7
>>> maximo([1,2,3,4])
4
>>> maximo([-5,4])
4
>>> maximo([-5,-4])
0
¿Por qué falla en el último caso? ¿Por qué anda en el caso anterior? ¿Cómo se puede inicializar m para que la función ande también con números negativos? Corregilo y guarda la versión mejorada en el archivo busqueda_en_listas.py.

Si te dan ganas, agregá una función minimo() al archivo.
"""

def maximo(lista):
    m = 0 # referencia
    for x in lista:
        if m <= x or m >= x:
            m = x
    return m

maximo = maximo([-5, -4, -3, 10])
print(maximo)

def minimo(lista):
    i = 0 # contador
    for x in lista:
        if i == 0: # referencia
            m = x
        if x < m:
            m = x
        i += 1
    return m

minimo = minimo([-5, -4, -3, 10])
print(minimo)
